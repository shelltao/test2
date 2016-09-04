# coding:utf-8

import json


def dumps(data):
    dump_data = json.dumps(data)

    print dump_data, type(dump_data)
    return dump_data


def load(data):
    load_data = json.loads(data)
    print load_data, type(load_data)


if __name__ == '__main__':
    person = {
        'name': '胡阳',
        'age': 20,
    }

    data = dumps(person)
    with open('json.data', 'w') as f:
        f.write(data)
    load(data)

    print '------'
    print

    persons = [person for i in range(10)]
    data = dumps(persons)
    load(data)
