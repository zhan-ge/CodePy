# -*- coding: utf-8 -*-
"""
    Project: 对切片命名
    Purpose: 内置的slice函数返回切片对象
    Version:
    Author:  ZG
    Date:    15/6/9
"""

if __name__ == '__main__':
    SRCCODE = '1213378923572983742934798237429834723942783429847923'
    SHARES = slice(20, 30)          # 对固定位置的切片进行命名，再多处使用时更清晰
    PRICE = slice(40, 45)

    my_shares = SRCCODE[SHARES]
    print my_shares

    my_price = SRCCODE[PRICE]
    print my_price
