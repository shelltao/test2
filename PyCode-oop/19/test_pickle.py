# coding:utf-8

import pickle


class Student(object):

    def __init__(self, name):
        self.name = name


def main():
    person = {
        'name': '胡阳',
        'age': 20,
    }
    data = pickle.dumps(person)
    print data

    stu = Student('test')
    stu_data = pickle.dumps(stu)
    print stu_data

    obj = pickle.loads(stu_data)
    print obj
    print obj.name


if __name__ == '__main__':
    main()
