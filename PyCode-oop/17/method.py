# coding:utf-8


class DB(object):
    name = 'line'

    @classmethod
    def get_instance(cls):
        print 'hi'

    @staticmethod
    def hello():
        print 'hi'


# 设计模式   单例模式

DB.get_instance()
DB.hello()
