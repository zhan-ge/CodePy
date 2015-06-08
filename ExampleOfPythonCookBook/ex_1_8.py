# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/8
"""

if __name__ == '__main__':
    prices = {
        'APPL': 34.23,
        'ACME': 23.89,
        'IBM': 58.22,
        'HPQ': 92.45,
        'FB': 73.12,
    }

    min_price = min(zip(prices.values(), prices.keys()))    # 最便宜的股票
    print min_price

    max_price = max(zip(prices.values(), prices.keys()))    # 最贵的股票
    print max_price

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print prices_sorted

    # zip()创建了一个迭代器，只能被消费一次，因此zip()的返回值只能被使用一次

    print min(prices, key=lambda k: prices[k])              # 价格最低的股票名
    print max(prices, key=lambda k: prices[k])              # 价格最高的股票名

    print prices[max(prices, key=lambda k: prices[k])]      # 价格最高的股票的价格