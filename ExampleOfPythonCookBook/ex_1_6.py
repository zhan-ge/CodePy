# -*- coding: utf-8 -*-
"""
    Project: 在字典中将键映射到多个值上
    Purpose: 实现 一键多值字典
    Version:
    Author:  ZG
    Date:    15/6/8
"""

from collections import defaultdict


if __name__ == '__main__':
    dict_set = defaultdict(set)         # 值为set类型的字典
    dict_list = defaultdict(list)         # 值为list类型的字典
    dict_tuple = defaultdict(tuple)         # 值为tuple类型的字典
    dict_dict = defaultdict(dict)         # 值为dict类型的字典
