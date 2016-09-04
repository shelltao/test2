# coding:utf-8

import sys
import os

tab = '----'


def write_file(line):
    with open('tree.txt', 'a') as f:
        import ipdb;ipdb.set_trace()
        f.write(line)
        f.write('\n')


def generate_tree(dir):
    for root, dirs, files in os.walk(dir):
        tab_num = root.count('/')
        if tab_num > 0:
            root = root.split('/')[-1]
        line = tab * tab_num + root

        write_file(line)

        tab_num += 1
        for f in files:
            line = tab * tab_num + f
            write_file(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print '你需要输入一个目录'
        exit()

    dir = sys.argv[1]
    generate_tree(dir)
