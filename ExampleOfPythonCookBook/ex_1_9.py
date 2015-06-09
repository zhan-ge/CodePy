# -*- coding: utf-8 -*-
"""
    Project: 在两个字典中寻找相同点
    Purpose: 寻找字典中相同的键或者相同的值
    Version:
    Author:  ZG
    Date:    15/6/9
"""

if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # 相同的键
    sim_keys = (a.keys() & b.keys())
    print sim_keys

    # 在a中但不在b中的键
    a.keys() - b.keys()

    # 相同的键值对
    a.items() & b.items()