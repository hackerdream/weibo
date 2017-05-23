
#!flask/bin/python
# encoding: utf-8
from flask import Blueprint


manage = Blueprint('manage', __name__, template_folder='templates', static_folder='static')


from . import views