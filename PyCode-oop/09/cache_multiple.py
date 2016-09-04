# coding:utf-8

def wrapper(func):
    cache = {}

    def inner_wrapper(number):
        key = number
        try:
            result = cache[key]
            print 'hit'
        except KeyError:
            result = func(number)
            cache[key] = result

        return result
    return inner_wrapper


#@wrapper
def multiple(number):
    result = 1
    for i in range(1, number):
        result = result * i
    return result

multiple = wrapper(multiple)


print multiple(10)
print multiple(10)
print multiple(10)
print multiple(20)
print multiple(20)
