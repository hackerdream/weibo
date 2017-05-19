#!flask/bin/python
# encoding: utf-8

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_uploads import  UploadSet, configure_uploads, IMAGES, patch_request_class
from flask import current_app

app = current_app._get_current_object()
photos =UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

class AddArticleForm(Form):
    text = TextAreaField('text',validators=[DataRequired(message=u'必填项'), Length(1, 140, message=u'不能超过140字')])
    photo = FileField('image', validators=[FileRequired(),FileAllowed(photos, 'you can only upload images')])
    submit = SubmitField('ok')

class DeletefollowedForm(Form):
    followed_id = StringField(validators=[DataRequired()])

class DeleteArticleForm(Form):
    article_id = StringField(validators=[DataRequired()])