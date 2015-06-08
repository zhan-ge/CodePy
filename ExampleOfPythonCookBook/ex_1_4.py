# -*- coding: utf-8 -*-
"""
    Project: 找到最大的或最小的N个元素
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/8
"""

import heapq


if __name__ == '__main__':
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print heapq.nlargest(3, nums)                   # [42, 37, 23]  取三个最大的值
    print heapq.nsmallest(3, nums)                  # [-4, 2, 1]    取三个最小的值

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'APPL', 'shares': 50, 'price': 12.4},
        {'name': 'FB', 'shares': 10, 'price': 66.9},
        {'name': 'HPQ', 'shares': 200, 'price': 23.3},
        {'name': 'YHOO', 'shares': 45, 'price': 87.6},
        {'name': 'ACME', 'shares': 80, 'price': 21.2},
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])     # 接收一个key，分别求最便宜的和最贵的3个
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

    print cheap
    print expensive