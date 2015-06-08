# -*- coding: utf-8 -*-
"""
    Project: 将序列分解为单独的变量
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/8
"""

if __name__ == '__main__':
    p = (4, 5)
    x, y = p                                                # 分解元祖

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data                        # 分解列表

    name, shares, price, (year, month, day) = data          # 分解嵌套序列

    s = "HELLO"
    a, b, c, d, e = s                                       # 分解字符串，同样适用于文件、迭代器

    _, shares, price, _ = data                              # 丢弃无用的值
