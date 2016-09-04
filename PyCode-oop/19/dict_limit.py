# coding:utf-8


class LRUCacheDict(object):
    def __init__(self, max_size=10):
        self._cache = {}
        self._item_times = {}
        self.max_size = max_size

    def __getitem__(self, key):
        print 'call __getitem__', key
        times = self._item_times.get(key, 0)
        result = self._cache[key]
        self._item_times[key] = times + 1
        return result

    def __setitem__(self, key, value):
        print key, value
        self._cache[key] = value

        if len(self._cache.keys()) > self.max_size:
            mix_key = None
            times_tuple = sorted(key=lambda x: x[1], [(k, v) for k, v in self._item_times.items()])
            key, value = times_tuple[-1]
            self._cache.pop(key)


    def print_times(self):
        for k, v in self._item_times.items():
            print k, 'called times:', v


cache = LRUCacheDict()

cache['name'] = 'huyang'
cache['age'] = 18
print cache['name']
print cache['name']
print cache['name']
print cache['age']
cache['title'] = 'test'
cache.print_times()
