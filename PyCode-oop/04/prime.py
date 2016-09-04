# coding:utf-8

while True:
    num = raw_input('type an number:').strip()
    try:
        num = float(num)
    except ValueError:
        print 'Error Type'
        continue

    num = int(num)

    i = 2
    is_prime = False
    while i < num:
        for ii in range(2, i):
            if i % ii == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            print i, 'is prime'

        i += 1
    else:
        break
