# coding:utf-8

def wrapper(func):
    cache = {}
    def inner_wrapper(n):
        key = n
        try:
            result = cache[key]
            print 'hit'
        except KeyError:
            result = func(n)

        cache[key] = result
        return result

    return inner_wrapper


@wrapper
def fib(n):
    if n <= 2:
        return 1

    return fib(n-1) + fib(n-2)


print fib(10)
