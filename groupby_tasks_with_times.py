# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/12
"""

import time
import gevent.monkey
gevent.monkey.patch_socket()

import gevent
from gevent import Greenlet


def fetch(pid):

    gevent.sleep(pid)
    print 'In ', pid
    print 'Sleep ', pid
    return ''


def asynchronous():
    print time.localtime()
    times = [1, 3, 5, 9]
    threads = [Greenlet.spawn(fetch, i) for i in times]
    gevent.joinall(threads)
    times = [thread.value for thread in threads]
    print time.localtime()
    return '->'.join(times)

#
print('Asynchronous:')
asynchronous()
