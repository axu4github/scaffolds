# coding=utf-8

from flask import Blueprint
from flaskr.hellos import HelloWorld

apis = Blueprint("apis", __name__, url_prefix="/apis")


@apis.route("/hello", methods=("GET", ))
def hello():
    return HelloWorld().say()
