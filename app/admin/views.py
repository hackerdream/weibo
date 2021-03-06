#!flask/bin/python
# encoding: utf-8
from flask import request, render_template, jsonify, redirect, url_for, g, flash
from flask_login import login_required, current_user
from . import admin
from .forms import CommentForm
from ..models import User, Follow, Article, get_articles, Comment, Photo
from .. import db
from sqlalchemy import and_
import json


@admin.before_request
def before_request():
    g.user = current_user


@admin.route('/weibo', methods=['GET', 'POST'])
@login_required
def homepage():
    return render_template('src/views/weibo.html')


@admin.route('/weibo/article', methods=['GET'])
@login_required
def get_weibo():
    follows = Follow.query.filter_by(follower_id=g.user.id)
    articles = get_articles(follows)
    marticles = Article.query.filter_by(host_id=g.user.id)
    for marticle in marticles:
        imgs = Photo.query.filter_by(article_id=marticle.id)
        photo = []
        for img in imgs:
            one = {'url': img.url}
            photo.append(one)
        comments = Comment.query.filter(and_(Comment.article_id == marticle.id, Comment.comment_type == 'rep'))
        repeat = []
        for comment in comments:
            r_comments = Comment.query.filter_by(reply=comment)
            r_repeat = []
            for r_comment in r_comments:
                onr = {'text': r_comment.text, 'time': r_comment.time, 'host_name': r_comment.host_name}
                r_repeat.append(onr)
            onc = {'text': comment.text, 'time': comment.time, 'host_nmae': comment.host_name,
                   'repeat': r_repeat, 'isShow': False}
            repeat.append(onc)
        tmp = {"host": g.user.name, "text": marticle.text, "up": marticle.up, "time": marticle.time, 'photo': photo,
               'repeat': repeat, 'isShow': False}
        articles.append(tmp)
    return jsonify(articles)


@admin.route('/weibo/user', methods=['GET'])
@login_required
def get_host():
    host = User.query.filter_by(id=g.user.id).first()
    name = {"name": host.name, 'id': host.id}
    namedata = dict(name)
    return jsonify(namedata)


@admin.route('/repeat', methods=['GET'])
def repeat():
    return jsonify({"repeat": False})


@admin.route('/admin/article_details/<article_id>', methods=['GET', 'POST'])
@login_required
def article_details(article_id):
    article = Article.query.get_or_404(int(article_id))
    form = CommentForm(request.form)
    if form.validate_on_submit():
        comment = Comment(article=article,
                          host_name=g.user.name,
                          text=form.text.data)
        db.session.add(comment)
        db.session.commit()
        followed_id = int(form.follow.data)
        if followed_id != -1:
            followed = Comment.query.get_or_404(id=followed_id)
            comment.comment_type = 'reply'
            comment.reply_to = followed.host_name
            db.session.add(comment)
            db.session.commit()
        flash(u'提交评论成功！', 'success')
        return redirect(url_for('.article_details', article_id=article.id))
    if form.errors:
        flash(u'发表评论失败', 'danger')
    host = User.query.filter_by(id=article.host_id).first()
    comments = article.comments.order_by(Comment.time.desc())
    return render_template('activity_details.html',
                           article=article, host=host, comments=comments)


@admin.route('/admin/article_details/<article_id>', methods=['GET', 'POST'])
@login_required
def vote(article_id):
    article = Article.query.get_or_404(int(article_id))
    article.new_up(article, db)
    article = Article.query.get_or_404(int(article_id))
    host = User.query.filter_by(id=article.host_id).first()
    comments = article.comments.order_by(Comment.time.asc())
    return render_template('activity_details.html',
                           article=article, host=host, comments=comments)


@admin.route('/main/addf/<int:mid>', methods=['GET', 'POST'])
@login_required
def add_follow(mid):
    follow = Follow(followed_id=mid,
                    follower_id=g.user.id)
    db.session.add(follow)
    db.session.commit()
    flash('success')
    return render_template('src/views/main.html')


@admin.route('/main/delf/<int:mid>', methods=['GET', 'POST'])
@login_required
def delete_followed(mid):
    follow = Follow.query.filter_by(followed_id=mid)
    for one in follow:
        if one.follower_id == g.user.id:
            db.session.delete(one)
            db.session.commit()
            return render_template('src/views/main.html')


@admin.route('/main/iff/<int:mid>', methods=['GET', 'POST'])
@login_required
def if_follow(mid):
    m = Follow.query.filter(and_(Follow.follower_id == g.user.id, Follow.followed_id == mid)).first()
    if m is not None:
        data = {"judge": True}
        return jsonify(data)
    return jsonify({"judge": False})


@admin.route('/admin/search', methods=['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('admin.homepage'))
    return redirect(url_for('admin.search_results', query=g.search_form.search.data))


@admin.route('/admin/search_results/<query>')
@login_required
def search_results(query):
    results = Article.query.whoosh_search(query, 50).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)


@admin.route('/main/<int:mid>', methods=['GET', 'POST'])
def main(mid):
    return render_template('src/views/main.html')


@admin.route('/main/<int:mid>/user', methods=['GET'])
def mainname(mid):
    host = User.query.filter_by(id=mid).first()
    name = {"name": host.name, 'id': host.id}
    namedata = dict(name)
    print namedata;
    return jsonify(namedata)


@admin.route('/main/<int:mid>/article', methods=['GET', 'POST'])
def showmain(mid):
    marticles = Article.query.filter_by(host_id=mid)
    m = User.query.filter_by(id=mid).first()
    articles = []
    for marticle in marticles:
        imgs = Photo.query.filter_by(article_id=marticle.id)
        photo = []
        for img in imgs:
            one = {'url': img.url}
            photo.append(one)
        tmp = {"host": m.name, "text": marticle.text, "up": marticle.up, "time": marticle.time, 'photo': photo}
        articles.append(tmp)
    return jsonify(articles)
