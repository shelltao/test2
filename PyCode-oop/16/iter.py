# coding:utf-8


class MyRange(object):
    def __init__(self, start, max):
        self.num = start
        self.max = max

    def __iter__(self):
        print self
        return self

    def next(self):
        if self.num < self.max:
            num = self.num
            self.num += 1
            return num

        raise StopIteration()


s = MyRange(0, 10)

for i in s:
    print i
