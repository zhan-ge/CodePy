# -*- coding: utf-8 -*-
"""
    Project: 从任意长度的可迭代对象中分解元素
    Purpose: 
    Version: Only support in python 3.
    Author:  ZG
    Date:    15/6/8
"""


def drop_first_last(grades):
    middle = []
    # first, *middle, last = grades
    # return avg(middle)                                  # middle=[57, 78, 68, 92]


if __name__ == '__main__':
    grades_all = [99, 57, 78, 68, 92, 71]
    # grades_avg = drop_first_last(grades_all)

    record = ['Dave', 'dave@example.com', '773-555-1212', '712-232-2332']
    # name, email, *phone_numbers = record                # phone_numbers=['773-555-1212', '712-232-2332']
