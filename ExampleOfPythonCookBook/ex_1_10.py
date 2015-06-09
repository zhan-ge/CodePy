# -*- coding: utf-8 -*-
"""
    Project: 从序列中移除重复项且保持剩下元素间顺序不变
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/9
"""

def dedupe(items):                      # 使用集合和生成器
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_new(items, key=None):        # 复杂数据结构，如嵌套字典的去重
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    L = [1, 2, 4, 5, 2, 3, 5, 3, 4]
    Ls = list(dedupe(L))
    print Ls

    D = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    Ds = list(dedupe_new(D, lambda d:(d['x'], d['y'])))     # 按 x键和y键去重
    print Ds

    Dss = list(dedupe_new(D, lambda d: d['x']))             # 按 x键去重
    print Dss

    Lss = list(dedupe_new(L))                               # 新的去重函数同样适用于简单列表
    print Lss

    with open('log.log') as f:                              # 对文本行去重
        for line in dedupe_new(f):
            print line
