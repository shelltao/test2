# coding:utf-8

cache = {}

while True:
    num = raw_input('type an number:').strip()
    try:
        num = float(num)
    except ValueError:
        print 'Error Type'
        continue

    num = int(num)

    result = cache.get(num)
    if result:
        print 'hit'
        print result
        continue
    else:
        print 'miss'

    is_prime = False
    for ii in range(2, num):
        print 'jisuan', ii
        if num % ii == 0:
            is_prime = False
            break
        else:
            is_prime = True

    msg = ""
    if is_prime:
        msg = '%d is prime' % num
    else:
        msg = '%d is not prime' % num
    cache[num] = msg
    print msg
