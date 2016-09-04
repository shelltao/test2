# coding:utf-8

import os


rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=True):
    print(dirName)
    for fname in fileList:
        print('\t%s' % fname)
    print '-------------'
