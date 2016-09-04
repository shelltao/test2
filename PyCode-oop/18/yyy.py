# coding:utf-8


def say():
    for i in range(10):
        t = yield i
        print t


t = say()
t.next()
for i in range(10, 20):
    print t.send(i)
