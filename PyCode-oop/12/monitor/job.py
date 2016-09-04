# coding:utf-8
import time
import psutil


def get_sys_info():
    result = {
        'cpu_percent': psutil.cpu_percent(),
        'mem_percent': psutil.virtual_memory().percent,
        'net_out': psutil.net_io_counters().bytes_sent,
        'net_in': psutil.net_io_counters().bytes_recv,
    }

    return result


if __name__ == '__main__':
    data = get_sys_info()
    cpu_percent = str(data.get('cpu_percent')) + '%'
    mem_percent = str(data.get('mem_percent')) + '%'
    net_in = str(data.get('net_in') / 1024 / 1024) + 'M'
    net_out = str(data.get('net_out') / 1024 / 1024) + 'M'

    cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('monitor.log', 'a') as f:
        line = '%s %s %s %s %s\n' % (cur_time, cpu_percent, mem_percent, net_in, net_out)
        f.write(line)
        f.flush()
