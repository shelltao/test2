# coding:utf-8

import random

num = random.randint(0, 9)

while True:
    user_num = raw_input("please type a number:")
    user_num = int(user_num)

    if user_num == num:
        print 'succes'
        for i in range(1, 8):
            print '*' * i
        break
    else:
        print 'error'
        
