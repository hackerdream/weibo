#!flask/bin/python
# encoding: utf-8

from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional

class CommentForm(Form):
    text = TextAreaField('comment', validators=[DataRequired(), Length(1, 140)])
    follow = StringField(validators=[DataRequired()])