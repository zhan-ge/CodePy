# -*- coding: utf-8 -*-
"""
    Project: 让字典保持有序
    Purpose: 内部使用双向列表维护顺序，是普通字典大小的两倍
    Version:
    Author:  ZG
    Date:    15/6/8
"""

import simplejson as json
from collections import OrderedDict


if __name__ == '__main__':
    d = OrderedDict()               # 有序字典，会按添加的顺序往后排
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    print d

    # 保持顺序然后做序列化
    parms = json.dumps(d)
    print parms