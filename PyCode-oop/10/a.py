# coding:utf-8
"""
做菜姑娘
"""

__all__ = ['chaocai']


def chaocai(cai):
    print cai
    qiecai(cai)
    dianhuo(cai)
    fanchao(cai)
    zhuangpan(cai)


def qiecai(cai):
    print 'qiecai', cai

def dianhuo(cai):
    print 'dianhuo', cai


def fanchao(cai):
    print 'fanchao', cai

def zhuangpan(cai):
    print 'zhuangpan', cai


if __name__ == '__main__':
    from b import maicai
    cai = maicai('baicai')
    chaocai(cai)
