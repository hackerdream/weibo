#!flask/bin/python
# encoding: utf-8
from flask import request, render_template, json, redirect, url_for, g, flash
from flask_login import login_required, current_user
from . import admin
from .forms import CommentForm
from ..models import User, Follow, Article, get_articles, Comment
from .. import db

@admin.before_request
def before_request():
  g.user = current_user

@admin.route('/admin', methods=['GET', 'POST'])
@admin.route('/admin/homepage', methods=['GET', 'POST'])
@admin.route('/admin/homepage/<int:page>', methods=['GET', 'POST'])
@login_required
def homepage(page=1):
    follows = Follow.query.filter_by(follower_id=g.user.id)
    host = User.query.filter_by(id=g.user.id).first()
    pagination = follows.paginate(page, 2, False)
    articles = get_articles(pagination.items)
    return render_template('admin/homepage.html', articles=articles, host=host,
                            pagination=pagination,endpoint='admin.homepage', page=page)

@admin.route('/admin/article_details/<article_id>', methods=['GET', 'POST'])
@login_required
def article_details(article_id):
    article =Article.query.get_or_404(int(article_id))
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
    article =Article.query.get_or_404(int(article_id))
    article.new_up(article, db)
    article = Article.query.get_or_404(int(article_id))
    host = User.query.filter_by(id=article.host_id).first()
    comments = article.comments.order_by(Comment.time.asc())
    return render_template('activity_details.html',
                           article=article, host=host, comments=comments)

@admin.route('/admin/follow/<user_id>', methods=['GET', 'POST'])
@login_required
def add_follow(user_id):
    follow = Follow(followed_id=user_id,
                    follower_id=g.user.id)
    db.session.add(follow)
    db.session.commit()
    flash('success')
    return redirect(url_for('admin.homepage'))

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

@admin.route('/admin/<user_id>', method=['GET','POST'])
@admin.route('/admin/<user_id>/<page>', method=['GET','POST'])
def show_one(user_id,page=1):
    articles = Article.query.filter_by(host_id=user_id).order_by(Article.time.desc())
    host = User.query.filter_by(id=g.user.id).first()
    pagination = articles.paginate(page, 2, False)
    return render_template('admin.homepage.html', page=page, pagination=pagination, host=host,
                           articles=articles, endpoint='login.index')


