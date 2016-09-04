# coding:utf-8

from cache import cache_it


@cache_it
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

while True:
    raw_input()

if __name__ == '__main__':
    fib(10)
