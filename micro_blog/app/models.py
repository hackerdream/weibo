#!flask/bin/python
# encoding: utf-8

import hashlib
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager
from flask import current_app, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))
    avatar_hash = db.Column(db.String(32))
    confirmed = db.Column(db.Boolean, default=False)
    articles = db.relationship('Article', backref='host', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if  self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    def gravatar(self, size=40, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def generate_reset_password_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'password': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('password') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        db.session.commit()
        return True


    def change_name(self, new_name):
        if self.query.filter_by(name=new_name).first() is not None:
            return False
        self.name = new_name
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<User %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.Text(140))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    up = db.Colume(db.integer, default = 0)
    comments = db.relationship('Comment', backref='article', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Article, self).__init__(**kwargs)

    def new_up(db):
        key = Article.query.first()
        key.up += 1

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_name = db.Column(db.Integer, db.ForeignKey('user.name'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    text = db.Column(db.Text(140))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    comment_type = db.Column(db.String(64), default='comment')
    reply = db.Column(db.String(128), default='notReply')

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super(Follow, self).__init__(**kwargs)

    def add(self):
        follow = Follow.query.filter_by(follower_id=self.follower_id).first()
        if follow is not None:
            pass
        else:
            db.session.add(self)


def get_articles(follows):
    articles = []
    for follow in follows:
        articles.append(Article.query.filter_by(Article.host_id==follow.followed_id).first())
    return articles