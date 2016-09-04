# coding:utf-8
t = 'abc'
r = ''

# 加密
for i in t:
    r += chr(ord(i) << 1)
    # r = r + chr(ord(i) << 1)

print r

new_t = ''
# 解密
for i in r:
    new_t += chr(ord(i) >> 1)

print new_t
