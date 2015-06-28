# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/28
"""

import simplejson as json

from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps
import time

import tornado.ioloop
import tornado.web

EXECUTOR = ThreadPoolExecutor(max_workers=4)

def unblock(f):
    @tornado.web.asynchronous
    @wraps(f)
    def wrapper(*args, **kwargs):
        self = args[0]

        def callback(future):
            self.write(future.result())
            self.finish()

        EXECUTOR.submit(
            partial(f, *args, **kwargs)
        ).add_done_callback(
            lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                partial(callback, future)
            )
        )

    return wrapper


class MainHandler(tornado.web.RequestHandler):

    @unblock
    def get(self):
        # self.write("hello world %s" % time.time())
        time.sleep(0.1)
        self.set_header("Content-Type", "text/json")
        return json.dumps({'result': 'hello'})


class SleepHandler(tornado.web.RequestHandler):

    @unblock
    def get(self, n):
        time.sleep(float(n))
        # return "Awake! %s" % time.time()
        return "Awake! %s" % n


class SleepAsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, n):

        def callback(future):
            self.write(future.result())
            self.finish()

        EXECUTOR.submit(
            partial(self.get_, n)
        ).add_done_callback(
            lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                partial(callback, future)
            )
        )

    def get_(self, n):
        time.sleep(float(n))
        return "Awake! %s" % time.time()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/sleep/(\d+)", SleepHandler),
            (r"/sleep_async/(\d+)", SleepAsyncHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
