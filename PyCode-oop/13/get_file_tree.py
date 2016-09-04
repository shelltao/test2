# coding:utf-8

import os


result = {}


def construct_tree(top, dirs, files):
    keys = top.split('/')
    tmp_top_path = result
    for key in keys:
        print key
        tmp_top_path = tmp_top_path.get(key, [])

    for filename in files:
        tmp_top_path.append(filename)
    print tmp_top_path


def parse_walk(arg, top, names):
    dirs = filter(lambda x: os.path.isdir(x), names)
    files = set(names) - set(dirs)

    construct_tree(top, dirs, files)


def main():
    os.path.walk('.', parse_walk, None)

    print result


if __name__ == '__main__':
    main()
