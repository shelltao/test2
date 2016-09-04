# coding:utf-8

from db import get_db, save_db, Student


def choice():
    while True:
        command = raw_input('输入执行(add/read/delete/update):')
        try:
            handler = CURD_MAP[command]
            handler()
        except KeyError:
            print '命令[%s]不存在' % command


def read(no=None):
    if not no:
        try:
            no = int(raw_input('输入学号进行查询，学号:'))
        except TypeError:
            print '类型错误，请重新输入'
            read()

    db = get_db()

    student = db.get(no)
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

    db = get_db()
    if db:
        no = max(db.keys()) + 1  # 编号递增
    else:
        no = 1

    columns.insert(0, no)
    student = Student(*columns)
    db[no] = student

    save_db(db)


def delete(no=None):
    if not no:
        try:
            no = int(raw_input("输入学员编号:"))
        except TypeError:
            print '编号类型错误'
            delete()

    db = get_db()
    try:
        student = db.pop(no)
        print '删除[%s]成功' % student.name
    except KeyError:
        print '编号不存在'
        delete()

    save_db(db)


def update(no=None):
    if not no:
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

    db = get_db()

    columns.insert(0, no)
    student = Student(*columns)

    db[no] = student

    save_db(db)


CURD_MAP = {
    'read': read,
    'add': add,
    'delete': delete,
    'update': update,
}


if __name__ == '__main__':
    choice()
