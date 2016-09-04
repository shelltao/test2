# coding:utf-8
from time import time
from collections import OrderedDict  # dict 无序的


# doctest

class LRUCacheDict(object):
    """ A dictionary-like object, supporting LRU caching semantics.
    >>> d = LRUCacheDict(max_size=3, expiration=3)
    >>> d['foo'] = 'bar'
    >>> d['foo']
    'bar'
    >>> import time
    >>> time.sleep(4) # 4 seconds > 3 second cache expiry of d
    >>> d['foo']
    Traceback (most recent call last):
        ...
    KeyError: 'foo'
    >>> d['a'] = 'A'
    >>> d['b'] = 'B'
    >>> d['c'] = 'C'
    >>> d['d'] = 'D'
    >>> d['a'] # Should return value error, since we exceeded the max cache size
    Traceback (most recent call last):
        ...
    KeyError: 'a'
    """
    def __init__(self, max_size=1024, expiration=15*60):
        self.max_size = max_size
        self.expiration = expiration

        self.__values = {}
        self.__expire_times = OrderedDict()
        self.__access_times = OrderedDict()

    def size(self):
        return len(self.__values)

    def clear(self):
        """
        Clears the dict.
        >>> d = LRUCacheDict(max_size=3, expiration=1)
        >>> d['foo'] = 'bar'
        >>> d['foo']
        'bar'
        >>> d.clear()
        >>> d['foo']
        Traceback (most recent call last):
        ...
        KeyError: 'foo'
        """
        self.__values.clear()
        self.__expire_times.clear()
        self.__access_times.clear()

    def has_key(self, key):
        """
        This method should almost NEVER be used. The reason is that between the time
        has_key is called, and the key is accessed, the key might vanish.
        You should ALWAYS use a try: ... except KeyError: ... block.
        >>> d = LRUCacheDict(max_size=3, expiration=1)
        >>> d['foo'] = 'bar'
        >>> d['foo']
        'bar'
        >>> import time
        >>> if d.has_key('foo'):
        ...    time.sleep(2) #Oops, the key 'foo' is gone!
        ...    d['foo']
        Traceback (most recent call last):
        ...
        KeyError: 'foo'
        """
        return key in self.__values

    def __setitem__(self, key, value):
        t = int(time())
        self.__delete__(key)
        self.__values[key] = value
        self.__access_times[key] = t
        self.__expire_times[key] = t + self.expiration
        self.cleanup()

    def __getitem__(self, key):
        t = int(time())
        del self.__access_times[key]
        self.__access_times[key] = t
        self.cleanup()
        return self.__values[key]

    def __delete__(self, key):
        if key in self.__values:
            del self.__values[key]
            del self.__expire_times[key]
            del self.__access_times[key]

    def cleanup(self):
        if self.expiration is None:
            return None
        t = int(time())
        # Delete expired
        for k in self.__expire_times.iterkeys():
            if self.__expire_times[k] < t:
                self.__delete__(k)
            else:
                break

        while (len(self.__values) > self.max_size):
            for k in self.__access_times.iterkeys():
                self.__delete__(k)
                break


def lru_cache_function(max_size=1024, expiration=60):
    cache = LRUCacheDict(max_size=max_size, expiration=expiration)

    def cache_it(func):
        def wrap(num):
            key = num
            try:
                result = cache[key]
                print 'hit'
            except KeyError:
                print 'not hit', key
                result = func(num)
                cache[key] = result

            return result

        return wrap
    return cache_it


@lru_cache_function(2)
def example(num):
    return num * 1000 / 4.3 * 50


if __name__ == '__main__':
    example(10)
    example(20)
    example(30)

    example(30)
    example(20)
    example(10)
