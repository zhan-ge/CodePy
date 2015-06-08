# -*- coding: utf-8 -*-
"""
    Project: 实现优先级队列
    Purpose: 实现一个队列，能够根据给定的优先级对元素排序，每次pop时总是返回优先级最高的元素
    Version:
    Author:  ZG
    Date:    15/6/8
"""

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        try:
            return heapq.heappop(self._queue)[-1]
        except IndexError:
            return None


if __name__ == '__main__':
    q = PriorityQueue()
    q.push('1111', 1)
    q.push('2222', 2)
    q.push('3333', 3)
    q.push('4444', 4)
    q.push('4444', 4)
    print q.pop()
    print q.pop()
    print q.pop()
    print q.pop()
    print q.pop()
    print q.pop()