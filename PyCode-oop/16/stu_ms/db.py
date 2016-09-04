# coding:utf-8

from collections import namedtuple

Student = namedtuple("Student", ['no', 'name', 'sex', 'age', 'location', 'qq'])


DB_PATH = 'stu.db'


def get_db(path=DB_PATH):
    struct_db = {}

    with open(path) as f:
        for line in f:
            columns = line.split()
            no = int(columns[0])

            student = Student(*columns)

            struct_db[no] = student
            struct_db.keys()

    return struct_db


def save_db(students, path=DB_PATH):
    with open(path, 'w') as f:
        for stu in students.values():
            line = ' '.join(map(str, tuple(stu)))
            f.write(line + '\n')
