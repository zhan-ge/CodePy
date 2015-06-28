# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/28
"""


from tornado.httpclient import HTTPClient


# 一个同步函数的样例
def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


from tornado.httpclient import AsyncHTTPClient

# 一个用回调参数模式重写的异步函数的样例
def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        print 'In handle_response:'
        return response.body

    return http_client.fetch(url, callback=handle_response)


from tornado.concurrent import Future

def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result()))
    return my_future


# 引入协程库gen
from tornado import gen

# 使用gen.coroutine修饰器
@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    # 在Python 3.3版本之前，在生成器中是不允许有返回值的
    # （既不允许在有生成器的函数内，使用return语句，Python解释器会报错）
    # 所以，必须通过使用抛出异常的方式代替
    # 如使用 raise gen.Return(response.body）
    # return response.body
    raise gen.Return(response.body)


import gevent.monkey
gevent.monkey.patch_socket()

import requests
import gevent
from gevent import Greenlet


def fetch(pid):
    url = '/'.join(['http://localhost:8888/sleep', str(pid)])
    response = requests.get(url)
    result = response.content

    # print('Process %s: %s' % (pid, datetime))
    print result
    return result


def asynchronous():
    threads = [Greenlet.spawn(fetch, i) for i in range(10)]
    gevent.joinall(threads)
    # times = [thread.value for thread in threads]
    # return '->'.join(times)


def test_server():
    url = 'http://localhost:8888/'
    r = requests.get(url)
    print dir(r)
    print r.headers
    print type(r.content)


if __name__ == '__main__':
    urls = 'http://www.baidu.com'
    # print synchronous_fetch(urls)
    # print asynchronous_fetch(urls)
    # res = async_fetch_future(urls)
    # res = fetch_coroutine(urls)
    # print dir(res)
    # asynchronous()
    test_server()