# coding:utf-8
# coding=utf-8
# _*_code_*_:utf-8

import argparse
import os

parser = argparse.ArgumentParser(description='statistics the number of lines of code')
parser.add_argument('-p', '--path', default='.', dest='dirpath', type=str,
                    help='设定路径')
parser.add_argument('-l', '--language', default='python', dest='lang', type=str,
                    help='输入你想统计的语言，支持: python, ruby, c, java, 注：可以输入多个用英文逗号分隔')
parser.add_argument('-d', '--depth', default=1, dest='depth', type=int,
                    help='想要遍历的深度, 默认是1')


BAN_TEXT = [
    '#coding:',
    '#coding=',
    '#_*_coding=',
]

LANG_POSTFIX = {
    'python': '.py',
    'java': '.java',
    'ruby': '.rb',
    'c': '.c'
}


def collect_files(path, depth):
    """
    收集所有的文件，包含路径
    """
    list_files = []

    def recurse_dir(_path, _depth):
        if _depth < 1:
            return None

        for d in os.listdir(_path):
            full_path = os.path.join(_path, d)
            if os.path.isfile(full_path):
                list_files.append(full_path)
            else:
                recurse_dir(full_path, _depth-1)

    recurse_dir(path, depth)

    return list_files


def statics_by_lang(lang, files):
    result = {}
    postfix = LANG_POSTFIX.get(lang)
    if not postfix:
        return None

    real_files = filter(lambda x: x.endswith(postfix), files)
    for file_name in real_files:
        result[file_name] = parse_file(file_name)

    return result


def parse_file(file_name):
    comment_count = 0  # 测试注释
    code_count = 0
    blank_count = 0

    with open(file_name) as f:
        multi_flag = False
        multi_count = 0

        for line in f:
            line = line.strip('\n').strip()

            if not multi_flag and is_comment(line):
                comment_count += 1

            elif (line.startswith("'''") or line.startswith('"""')) and (line.endswith('"""') or line.endswith("'''")):
                comment_count += 1

            elif not multi_flag and (line.startswith("'''") or line.startswith('"""')):
                multi_flag = True
                if len(line) > 3:
                    multi_count += 1

            elif multi_flag and (line.endswith("'''") or line.endswith('"""')):
                if len(line) > 3:
                    multi_count += 1

                multi_flag = False
                comment_count += multi_count
                multi_count = 0

            elif multi_flag and line:
                multi_count += 1

            elif line == '':
                # 处理空行
                blank_count += 1
            else:
                # 剩余的就是有效代码
                code_count += 1

    return comment_count, blank_count, code_count


def is_comment(line):
    """
    判断是否为注释行:
    规则：
        1. 以#开头
        2. 结尾注释有 # ，并且不是被写在字符串中的
    """
    if line.startswith('#'):
        return True

    if '#' in line:
        line = line.rsplit('#', 1)[-1]
        if '\'' not in line and '\"' not in line:
            return True

    return False


def main():
    args = parser.parse_args()

    files = collect_files(args.dirpath, args.depth)
    results = statics_by_lang(args.lang.lower(), files)
    for file_name, value in results.items():
        print file_name
        print '\t注释: %s, 空行:%s, 代码行数:%s' % value

    sum_values = zip(*results.values())
    print '总计:'
    print '\t注释:%s, 空行:%s, 代码行数:%s' % tuple(map(sum, sum_values))


if __name__ == '__main__':
    main()
