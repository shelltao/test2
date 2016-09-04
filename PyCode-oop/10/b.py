# coding:utf-8
from xiaoyemasha import chaocai, qiecai, zuofan, 

import a.chaocai


def chaocai(cai):
    a.chaocai(cai)
    print 'chaocai'


def maicai(cai):
    print 'maile', cai
    return cai


if __name__ == '__main__':
    cai = maicai('白菜')

    chaocai(cai)
