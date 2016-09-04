# coding:utf-8

import os

import psutil


def get_sys_info():
    result = {
        'cpu_core': psutil.cpu_count(),
        'mem': psutil.virtual_memory().percent,
        'uptime': psutil.boot_time(),
        'current_user': os.getlogin()
    }

    return result


if __name__ == '__main__':
    data = get_sys_info()
    with open('result.txt', 'w') as f:
        result = ['%s:%s' % (k, v) for k, v in data.items()]
        f.write(' '.join(result))
