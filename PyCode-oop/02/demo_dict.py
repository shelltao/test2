# coding:utf-8
d1 = {
    "a1": 1,
    "a2": 2,
    "a3": 3,
    "a4": 4,
    "a5": 5,
}

d2 = {
    "a4": 90,
    "a6": 5,
    "a1": 2,
    "a9": 8,
    "a8": 9,
}

# 1. 获取d1和d2key的交集，并以d2的值为主生成dict
result = {}
for k, v in d1.items():
    if k in d2:
        result[k] = d2[k]

print result

# 2. 去掉d1和d2中key重复以及value重复的值，合并成一个dict
new_d1 = d1

common_keys = set(d1.keys()) & set(d2.keys())
common_values = set(d1.values()) & set(d2.values())

new_d1.update(d2)

result = {}

for k, v in new_d1.items():
    if k not in common_keys and v not in common_values:
        result[k] = v

print result
