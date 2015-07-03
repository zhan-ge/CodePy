# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/7/3
"""

import os
os.environ['CLASSPATH'] = '/Users/ZG/Project/CodePy/lib/MainPartExtractor.jar'

from jnius import autoclass


if __name__ == '__main__':
    strings = u"小狗喜欢它的父亲和母亲"

    Extractor = autoclass('Extractors.Extractors')
    print dir(Extractor)

    # Those resources's path be absolute path.
    Extractor.setModel("testMainPartExtractors/chinesePCFG.ser", "testMainPartExtractors/userwords.txt")
    result = Extractor.trunkhankey(strings, "testMainPartExtractors/deprules.txt", False)
    print result
