# coding:utf-8

from db import DB, StoreError


class Student(object):
    def __init__(self, _id=None, name=None, sex=None,
                 age=None, location=None, qq=None):
        self.id = _id
        self.name = name
        self.sex = sex
        self.age = age
        self.location = location
        self.qq = qq

    @property
    def columns(self):
        """
            注意，返回字段不包括id
        """
        return [self.name, self.sex,
                self.age, self.location, self.qq]


class StudentManager(object):
    _db = DB()

    def __init__(self, db=None):
        self.db = db or self._db
        self.try_times = 0

    def find_one(self, _id):
        # TODO: 异常处理 Assert Error
        columns = self.db.query_by_id(_id)
        return Student(*columns)

    def update(self, student):
        try:
            self.db.update(student.id, student.columns)
        except StoreError as e:
            if self.try_times < 3:
                self.update(student)
                self.try_times += 1
            return {
                'status': 1,
                'msg': '保存时出错',
            }

        except Exception as e:
            return {
                'status': 2,
                'msg': '系统异常',
            }

        return {
            'status': 0,
            'msg': 'success',
        }

    def add_one(self, student):
        self.db.insert(student.columns)
        return True

    def delete(self, student):
        return self.db.delete_by_id(student.id)
