# coding:utf-8

s = """
Have you thought about what you want people to say about you after you’re gone? Can you hear the voice saying, “He was a great man.” Or “She really will be missed.” What else do they say?
One of the strangest phenomena of life is to engage in a work that will last long after death. Isn’t that a lot like investing all your money so that future generations can bare interest on it? Perhaps, yet if you look deep in your own heart, you’ll find something drives you to make this kind of contribution---something drives every human being to find a purpose that lives on after death.
"""

max_value = ord('z')
min_value = ord('A')

# 区分大小写
diff_result = {}
# 不区分大小写
result = {}

for char in s:
    if ord(char) > max_value or ord(char) < min_value:
        continue

    value = diff_result.setdefault(char, 0)
    diff_result[char] += 1

    value = result.setdefault(char.lower(), 0)
    result[char.lower()] += 1

print '一、区分大小写'
print '用到字母如下:'
print ','.join(diff_result.keys())
print '字母出现频率:'
sorted_diff_result = sorted(diff_result.items(), key=lambda x: x[1], reverse=True)
for k, v in sorted_diff_result:
    print k, v


print '二、不区分大小写'
print '用到字母如下:'
print ','.join(result.keys())
print '字母出现频率:'
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
for k, v in sorted_result:
    print k, v

"""
思考：

如何避免重复的逻辑，比如上面的两次统计，还有最后的两次输出
"""
