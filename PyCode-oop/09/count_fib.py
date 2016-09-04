# coding:utf-8

count = {'count': 0}
def wrapper(func):
    def inner_wrapper(n):
        count['count'] += 1
        result = func(n)
        return result

    return inner_wrapper


@wrapper
def fib(n):
    if n <= 2:
        return 1

    return fib(n-1) + fib(n-2)


print fib(3)
print count['count']
