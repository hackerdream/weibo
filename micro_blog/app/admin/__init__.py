#!flask/bin/python
# encoding: utf-8
from flask import Blueprint


admin = Blueprint('admin', __name__)

from . import views