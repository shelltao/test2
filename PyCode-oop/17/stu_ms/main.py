# coding:utf-8

import logging
import sys

import settings  # noqa  初始化log模块
from model import Student, StudentManager


logger = logging.getLogger(__name__)


manager = StudentManager()


def choice():
    while True:
        command_list = '/'.join(CURD_MAP.keys())
        command = raw_input('输入执行(%s):' % command_list)
        try:
            handler = CURD_MAP[command]
            handler()
        except KeyError:
            print '命令[%s]不存在' % command
            logger.info('命令[%s]不存在' % command)


def query():
    try:
        no = int(raw_input('输入学号进行查询，学号:'))
    except TypeError:
        print '类型错误，请重新输入'
        query()

    student = manager.find_one(no)

    if not student:
        print '不存在'
        return

    print student.name, student.age, student.sex, student.location


def add():
    info = raw_input('请输入学员信息(姓名，性别，年龄，所在地，qq号）各项信息之间用逗号分隔:')
    if ',' in info:
        columns = info.split(',')
    elif '，' in info:
        columns = info.split('，')

    columns.insert(0, None)
    student = Student(*columns)

    manager.add_one(student)


def delete():
    try:
        no = int(raw_input("输入学员编号:"))
    except TypeError:
        print '编号类型错误'
        delete()

    try:
        student = Student()
        student.id = no
        result = manager.delete(student)
        if result:
            print '删除[%s]成功' % no
    except KeyError:
        print '编号不存在'
        delete()


def update():
    try:
        no = int(raw_input("输入学员编号:"))
    except TypeError:
        print '编号类型错误'
        update()

    info = raw_input('请输入学员信息(姓名，性别，年龄，所在地，qq号）各项信息之间用逗号分隔:')
    if ',' in info:
        columns = info.split(',')
    elif '，' in info:
        columns = info.split('，')

    columns = map(str.strip, columns)

    columns.insert(0, no)
    student = Student(*columns)

    manager.update(student)

def exit():
    sys.exit()


CURD_MAP = {
    'query': query,
    'add': add,
    'delete': delete,
    'update': update,
    'exit': exit,
}


if __name__ == '__main__':
    choice()
