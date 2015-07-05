# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/7/5
"""

import optparse
import argparse
import json
from simplejson.scanner import JSONDecodeError


class MatchPattern(object):

    def __init__(self, data, method):
        self.method = method
        self.data = self.extract(data)
        pass

    @classmethod
    def extract(cls, data):
        try:
            data = json.loads(data)
        except JSONDecodeError:
            data = None
        return data

    def match(self):
        pass


def parse_args():
    parser = argparse.ArgumentParser(description="This is the pattern matcher.")
    parser.add_argument('-t', '--type', type=str, default='query', help="type to match")
    parser.add_argument('data', type=str, default=None, help="data to match")
    # parser.add_argument('-d', '--data', type=json.loads, default=None)

    options = parser.parse_args()
    print options
    # print dict(options.data)
    # print json.loads(options.data)

    return options

# {"data":{"list":["3IBPZJXEU1A1E16","3IBPZJXEU1BR516","3IBPZJXEU1CYJ16","3IBPZJXEU1DYE16","3IBPZJXEU1EUK16","3IBPZJXEU1FSM16"]},"bstatus":{"code":0,"des":"正常"}}

def parse_args_old():

    usage = """usage: %prog --type type json-data
    This is the pattern matcher.
    Run it like this:
        $ python MatchPattern.py --type <type> <json-data>
    """

    parser = optparse.OptionParser(usage)

    type_info = "The interface type to match."
    parser.add_option('-t', '--type', type='string', help=type_info, default='query')

    data_info = "The json-data to match."
    parser.add_option('-d', '--data', type='string', help=data_info, default=None)

    options, args = parser.parse_args()

    # print options.data
    # print args

    if not options.data:
        parser.error('Provide the json data would be match.')

    # if not MatchPattern.extract(data):
    #     parser.error('The data must be right formate, check the data.')

    return options


def main():
    parse_args()
    # options = parse_args()
    # print type(options.data)
    # print options.type


if __name__ == '__main__':
    main()
