# coding:utf-8

import re

# flake8:noqa

TEST_TEXT = """
127.0.0.1 - - [03/Aug/2015:04:37:54 +0000] "GET /static/xadmin/js/xadmin.main.js HTTP/1.0" 200 3401 "http://demo.xadmin.io/static/xadmin/js/xadmin.main.js" "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-Manager Mobile Safari/537.36" "101.226.51.229" "0.000"ms 
127.0.0.1 - - [03/Aug/2015:04:37:54 +0000] "GET /static/xadmin/vendor/jquery-ui/jquery.ui.effect.js HTTP/1.0" 200 31918 "http://demo.xadmin.io/static/xadmin/vendor/jquery-ui/jquery.ui.effect.js" "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-Manager Mobile Safari/537.36" "101.226.51.229" "0.230"ms 
127.0.0.1 - - [03/Aug/2015:04:37:55 +0000] "GET /static/xadmin/js/xadmin.plugin.themes.js HTTP/1.0" 200 3492 "http://demo.xadmin.io/static/xadmin/js/xadmin.plugin.themes.js" "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-Manager Mobile Safari/537.36" "101.226.51.229" "0.000"ms 
127.0.0.1 - - [03/Aug/2015:04:37:56 +0000] "GET /static/xadmin/vendor/jquery-ui/jquery.ui.sortable.js HTTP/1.0" 200 42543 "http://demo.xadmin.io/static/xadmin/vendor/jquery-ui/jquery.ui.sortable.js" "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-Manager Mobile Safari/537.36" "101.226.51.229" "1.470"ms 
127.0.0.1 - - [03/Aug/2015:04:37:56 +0000] "GET /static/xadmin/vendor/jquery-ui/jquery.ui.core.js HTTP/1.0" 200 8195 "http://demo.xadmin.io/static/xadmin/vendor/jquery-ui/jquery.ui.core.js" "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-Manager Mobile Safari/537.36" "101.226.51.229" "0.000"ms 
127.0.0.1 - - [03/Aug/2015:04:37:56 +0000] "GET /xadmin/password_reset/ HTTP/1.0" 200 3414 "-" "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-Manager Mobile Safari/537.36" "101.226.51.229" "0.030"ms 
"""

RE_EXP = r'\d+.\d+.\d+.\d+'
RE_IP = re.compile(RE_EXP)


def pre_compile():
    search = RE_IP.search(TEST_TEXT)

    if search:
        return search.group()

    return None


def direct_search():
    search = re.search(RE_EXP, TEST_TEXT)
    if search:
        return search.group()

    return None
