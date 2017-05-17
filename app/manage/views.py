#!flask/bin/python
# encoding: utf-8

from .forms import *
from ..models import Article,Comment, User, Follow
from flask import flash, redirect, url_for, request, render_template, g, current_app
from flask_login import login_required, current_user
from .. import db
from . import manage
import json
from ..register.views import send_email
from ..models import get_followed, get_follower

@manage.route('/manage/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    form = AddArticleForm()
    method = 'add'
    if form.validate_on_submit():
        text = form.text.data
        article = Article(text=text, host_id=current_user.id)
        db.session.add(article)
        db.session.commit()
        flash('success!')
        return redirect(url_for('manage.index'))
    return render_template('manage/add_article.html', form=form, method=method)

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

@manage.route('/manage/show_followed', methods=['GET', 'POST'])
@login_required
def show_followed():
    follow = Follow.quert.filter(follower_id=g.current_user.id).all()
    users = get_followed(follow)
    render_template('manage/show_followed.html', users=users)

@manage.route('/manage/delete_followed', methods=['GET', 'POST'])
@login_required
def delete_followed():
    form = DeletefollowedForm()
    if form.validate_on_submit():
        followed_id = int(form.followed_id.data)
        follow = Follow.query.filter(followed_id=followed_id, follower_id=g.current_user.id).scalar()
        db.session.delete(follow)
        db.session.commit()
        flash('success')
        return redirect(url_for('manage.show_followed'))

@manage.route('/manage/show_follower', methods=['GET', 'POST'])
@login_required
def show_follower():
    follow = Follow.quert.filter(followed_id=g.current_user.id).all()
    users = get_follower(follow)
    render_template('manage/show_follower.html', users=users)
