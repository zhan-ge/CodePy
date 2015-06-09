# -*- coding: utf-8 -*-
"""
    Project: 找出序列中出现次数最多的元素
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/6/9
"""

if __name__ == '__main__':
    items = [1,2,3,23,23,2,5,4,6,4,434534,56,34,2,32,4,46,5,7,8,45,3,5,6,3,2,4,4,67]

    from collections import Counter
    item_counts = Counter(items)
    print item_counts
    # Counter({4: 5, 2: 4, 3: 3, 5: 3, 6: 2, 23: 2, 32: 1, 1: 1, 7: 1,
    # 8: 1, 34: 1, 46: 1, 45: 1, 56: 1, 67: 1, 434534: 1})

    top_three = item_counts.most_common(3)      # 次数出现最多的前3项和出现的次数
    print top_three

    # Counter对象可以进行数学运算