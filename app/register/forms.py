#!flask/bin/python
# encoding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
  #  password2 = PasswordField('Confirm password', validators=[DataRequired()])


    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError(u'该邮箱已经注册')
    #
    # def validate_name(self, field):
    #     if User.query.filter_by(name=field.data).first():
    #         raise ValidationError(u'该用户名已存在')