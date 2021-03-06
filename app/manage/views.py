#!flask/bin/python
# encoding: utf-8

from .forms import *
from ..models import Article, Comment, User, Follow, Photo
from flask import flash, redirect, url_for, request, render_template, g, current_app, jsonify
from flask_login import login_required, current_user
from .. import db
from . import manage
import base64
from datetime import datetime
from sqlalchemy import and_

import json
from ..register.views import send_email


@manage.route('/weibo/write_article', methods=['GET', 'POST'])
@login_required
def add_article():
    data = request.get_json()
    text = data['text']
    temp = data['imgs']
    article = Article(text=text, host_id=current_user.id, time=datetime.now())
    db.session.add(article)
    db.session.commit()
    new_article = Article.query.order_by(Article.time.desc()).first()
    for img in temp:
        imgStr = img['base64'].split(',')[1]
        imgdata = base64.b64decode(imgStr)
        url = 'static/public/imgs/' + img['name']
        file = open('app/' + url, 'wb')
        file.write(imgdata)
        file.close()
        photo = Photo(url=url, article_id=new_article.id)
        db.session.add(photo)
        db.session.commit()
    return redirect(url_for('admin.homepage'))  #


@manage.route('/manage/manage_article', methods=['GET', 'POST'])
@login_required
def manage_article():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(host_id=current_user.id).order_by(Article.time.desc())
    pagination = articles.paginate(page, 3, False)
    form = DeleteArticleForm()
    return render_template('manage/manage_article.html', articles=articles, endpoint='manage.manage_article',
                           form=form, pagination=pagination, page=page)


@manage.route('/manage/delete_article', methods=['GET', 'POST'])
@login_required
def delete_article():
    form = DeleteArticleForm()
    if form.validate_on_submit():
        article_id = int(form.article_id.data)
        article = Article.query.get_or_404(id=article_id)
        comments = Comment.query.filter_by(article_id=article_id)
        for comment in comments:
            db.session.delete(comment)
        db.session.delete(article)
        db.session.commit()
        flash('success')
        return redirect(url_for('manage.manage_article', page=request.args.get('page', 1, type=int)))
    return redirect(url_for('manage.manage_article', page=request.args.get('page', 1, type=int)))


@manage.route('/manage/show_followed/<int:uid>', methods=['GET', 'POST'])
def show_followed(uid):
    follows = Follow.query.filter_by(follower_id=uid)
    date = []
    for follow in follows:
        u = User.query.filter_by(id=follow.followed_id).first()
        m = Follow.query.filter(and_(Follow.followed_id == uid, Follow.follower_id == u.id)).first()
        if m is not None:
            one = {"name": u.name, "id": u.id, "rel": u'互相关注'}
        else:
            one = {"name": u.name, "id": u.id, "rel": u'已关注'}
        date.append(one)
    return jsonify(date)


@manage.route('/manage/show_follower/<int:uid>', methods=['GET', 'POST'])
def show_follower(uid):
    follows = Follow.query.filter_by(follower_id=uid)
    date = []
    for follow in follows:
        u = User.query.filter_by(id=follow.follower_id).first()
        m = Follow.query.filter(and_(Follow.follower_id == uid, Follow.followed_id == u.id)).first()
        if m is not None:
            one = {"name": u.name, "id": u.id, "rel": u'互相关注'}
        else:
            one = {"name": u.name, "id": u.id, "rel": u'被关注'}
        date.append(one)
    return jsonify(date)