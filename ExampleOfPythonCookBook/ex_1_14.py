# -*- coding: utf-8 -*-
"""
    Project: 对源生不支持比较操作的对象排序
    Purpose: 对多个类的实例对象进行排序
    Version:
    Author:  ZG
    Date:    15/6/9
"""

class User:
    def __init__(self, user_id):
        self.id = user_id

    def __repr__(self):
        return 'User({})'.format(self.id)


if __name__ == '__main__':
    users = [User(22), User(74), User(11)]
    print users
    sorted_users = sorted(users, key=lambda d: d.id)
    print sorted_users

    from operator import attrgetter                         # 更快的attrgetter
    sorted_users_new = sorted(users, key=attrgetter('id'))
    print sorted_users_new