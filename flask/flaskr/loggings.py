# coding=utf-8

from flask import current_app
from logging.config import fileConfig

import logging
import os


class LoggableMixin(object):

    def __init__(self):
        logging_config_path = os.path.join(
            current_app.config["BASE_DIR"], "flaskr", "logging_config.ini")
        fileConfig(logging_config_path)
        self.logger = logging.getLogger()
