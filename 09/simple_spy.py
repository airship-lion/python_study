from urllib.request import urlopen

import gevent
import time

from gevent import monkey

monkey.patch_all()  # gevent对于url请求没有当成io操作，所以请求网络时不会自动切换协程，用monkey打补丁后可以修复


def fun(url):
    resp = urlopen(url=url)
    data = resp.read()
    print(url, len(data))
    # f = open('spy.html', 'wb')
    # f.write(data)
    # f.close()


li = [
    'https://www.zhihu.com/question/19560062',
    'http://mebook.cc/481.html',
    'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%8A%9B%E7%9A%84%E6%B8%B8%E6%88%8F&ie=utf-8&pn=100',
    'http://music.163.com/#/playlist?id=124518200',
    'https://github.com/',
    'http://jandan.net/',
    'http://192.168.1.134:8085/tnoa/Login/toMain'
]

liTask = []
for url in li:
    liTask.append(gevent.spawn(fun, url))

asyn_start = time.time()
gevent.joinall(liTask)
print('异步花费时间', time.time() - asyn_start)

syn_start = time.time()
for url in li:
    fun(url)
print('同步花费时间', time.time() - syn_start)
