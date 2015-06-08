# -*- coding: utf-8 -*-
"""
    Project: 保存最后N个元素
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/8
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)  # deque(maxlen=history)生成一个固定长度的队列，添加队列时如果队列已满则移除最老的项
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('some.txt') as f:
        for line, previous_lines in search(f, 'Python', 5):
            for pline in previous_lines:
                print pline,
            print line,
            print '-' * 20

    # 如果不设置maxlen的大小，则得到一个无边界的队列
    q = deque()
    q.append('task1')               # 添加队列
    q.appendleft('task2')

    q.pop()                         # 推出队列
    q.popleft()
    q.clear()                       # 清空
