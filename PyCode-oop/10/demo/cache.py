# coding:utf-8


def cache_it(func):
    cache = {}

    def inner_cache(*args, **kwargs):
        key = str(args) + str(kwargs)
        try:
            return cache[key]
        except KeyError:
            result = func(*args, **kwargs)
            cache[key] = result

            return result
    return inner_cache
