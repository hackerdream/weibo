
#!flask/bin/python
# encoding: utf-8
from flask import Blueprint


login = Blueprint('login', __name__, template_folder='templates', static_folder='static')


from . import views