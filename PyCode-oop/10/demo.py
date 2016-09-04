# coding:utf-8


__all__ = ('add', )

print 'hi'


def say():
    return 'hi'


def add(a, b):
    return a + b


if __name__ == '__main__':
    # 主模块才会执行下面代码
    print say()
