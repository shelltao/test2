# coding:utf-8

prime_cache_set = set()
not_prime_cache_set = set()


def is_number(number):
    try:
        number = float(number)
    except ValueError:
        print 'Error Type'
        return False

    return True


def is_prime(number):
    if number in prime_cache_set:
        print 'hit cache'
        return True
    elif number in not_prime_cache_set:
        print 'hit cache'
        return False

    for i in range(2, number):
        if num % i == 0:
            not_prime_cache_set.add(num)
            return False
    
    prime_cache_set.add(num)
    return True


while True:
    num = raw_input('type an number:').strip()
    if not is_number(num):
        continue

    num = int(float(num))

    if is_prime(num):
        print '%d is prime' % num
    else:
        print '%d is not prime' % num
