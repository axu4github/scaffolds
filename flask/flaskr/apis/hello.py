# coding=utf-8

from . import apis


@apis.route("/hello", methods=("GET", ))
def hello():
    return "Hello Api"
