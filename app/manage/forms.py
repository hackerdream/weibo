#!flask/bin/python
# encoding: utf-8

from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateTimeField, DateField
from wtforms.validators import DataRequired, Length, ValidationError

class AddArticleForm(Form):
    text = TextAreaField('text',validators=[DataRequired(message=u'必填项'), Length(1, 140, message=u'不能超过140字')])

class DeletefollowedForm(Form):
    followed_id = StringField(validators=[DataRequired()])

class DeleteArticleForm(Form):
    article_id = StringField(validators=[DataRequired()])