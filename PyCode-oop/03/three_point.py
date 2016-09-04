# coding:utf-8

num = raw_input("input number:")
num = int(num)
if num < 3:
    print 'number must larger then 3'

for i in range(1, num):
    print '*' * i
