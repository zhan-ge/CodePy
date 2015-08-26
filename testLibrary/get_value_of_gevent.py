# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/5
"""

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
from gevent import Greenlet

import urllib2
import simplejson as json

def fetch(pid):
    response = urllib2.urlopen('http://time.jsontest.com')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['time']

    # print('Process %s: %s' % (pid, datetime))
    return json_result['time']

def synchronous():
    for i in range(1, 10):
        fetch(i)

def asynchronous():
    threads = [Greenlet.spawn(fetch, i) for i in range(10)]
    gevent.joinall(threads)
    times = [thread.value for thread in threads]
    return '->'.join(times)

# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()