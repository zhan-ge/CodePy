# -*- coding: utf-8 -*-
"""
    Project: 通过公共键对字典进行排序
    Purpose:
    Version:
    Author:  ZG
    Date:    15/6/9
"""

if __name__ == '__main__':
    rows = [
        {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'Join', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    ]

    from operator import itemgetter

    rows_by_frame = sorted(rows, key=itemgetter('fname'))   # 按fname键排序，仍返回原有的数据结构
    print rows_by_frame

    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print rows_by_uid

    rows_by_fname_and_lname = sorted(rows, key=itemgetter('fname', 'lname'))    # 按多个键排序
    print rows_by_fname_and_lname

    rows_by_frame = sorted(rows, key=lambda d: d['fname'])   # 使用lambda排序，但是没有itemgettrt速度快
    print rows_by_frame
    rows_by_fname_and_lname = sorted(rows, key=lambda d: (d['fname'], d['lname']))    # 按多个键排序
    print rows_by_fname_and_lname

    mi = min(rows, key=itemgetter('uid'))       # uid最小的项
    print mi
    ma = max(rows, key=itemgetter('uid'))
    print ma
