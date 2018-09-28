# coding=utf-8

from flaskr.loggings import LoggableMixin


class HelloWorld(LoggableMixin):

    def say(self):
        self.logger.info("HelloWorld.say")
        return "Hello Api"
