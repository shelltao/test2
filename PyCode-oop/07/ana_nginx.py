# coding:utf-8
import time


def time_it(func):
    def inner_wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print time.time() - start
    return inner_wrap


def parse_params(line):
    # 第一步： 获取需要的数据转成合适的格式
    line = line.strip('\n').strip()
    cur_time = line.split(' ')[3][-8:]
    url = line.split(' ')[6]
    cost = line.split(' ')[-1]
    cost = cost.replace('ms', '').replace('"', '')
    cost = float(cost)
    return cur_time, url, cost


@time_it
def parse_cost_data(file_path):
    result = {}

    with open(file_path) as f:
        for line in f:
            cur_time, url, cost = parse_params(line)

            # 存储数据结构
            #result.get(url) -- > None
            exist_url_cost = result.get(url, 0)
            result[url] = max(exist_url_cost, cost)
    return result


@time_it
def parse_top_visit_data(file_path):
    result = {}

    with open(file_path) as f:
        for line in f:
            cur_time, url, cost = parse_params(line)

            # 存储数据结构
            times = result.get(url, 0)
            result[url] = times + 1

    return result


@time_it
def parse_data_by_hour(file_path):
    result = {}

    with open(file_path) as f:
        for line in f:
            cur_time, url, cost = parse_params(line)

            hour = cur_time.split(':')[0]
            # 存储数据结构
            times = result.get(hour, 0)
            result[hour] = times + 1

    return result


@time_it
def parse_data_by_url_type(file_path):
    result = {}
    count = 0

    with open(file_path) as f:
        for line in f:
            count += 1
            cur_time, url, cost = parse_params(line)
            url = url.split('?')[0]

            params = url.split('.')
            if len(params) < 2:
                continue

            postfix = params[-1]
            # 存储数据结构
            times = result.get(postfix, 0)
            result[postfix] = times + 1

    # for k, v in result.items():
        # result[k] = v * 1.0 / count

    return result


def print_list(l, limit=10, title=None):
    return
    top = l
    if title:
        print title

    if limit:
        top = top[:10]
    for k, v in top:
        print k, v


def main():
    file_path = 'access.log'
    # 第一题
    result = parse_cost_data(file_path)

    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print_list(sorted_result, limit=10, title="第一题")

    # 第二题
    result = parse_top_visit_data(file_path)
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print_list(sorted_result, limit=10, title="第二题")

    # 第三题
    result = parse_data_by_hour(file_path)
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    print_list(sorted_result, limit=None, title="第三题")

    # 第四题
    result = parse_data_by_url_type(file_path)
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print_list(sorted_result, limit=10, title="第四题")


if __name__ == '__main__':
    main()
