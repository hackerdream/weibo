#!flask/bin/python
# encoding: utf-8

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


class AddArticleForm(Form):
    text = TextAreaField('text', validators=[DataRequired(message=u'必填项'), Length(1, 140, message=u'不能超过140字')])
    imgs = FileField('imgs', validators=[FileRequired()])
    name = StringField()
    # imgs = TextAreaField('imgs', validators=[DataRequired()])


class DeletefollowedForm(Form):
    followed_id = StringField(validators=[DataRequired()])


class DeleteArticleForm(Form):
    article_id = StringField(validators=[DataRequired()])
