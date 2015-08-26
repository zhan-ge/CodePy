# -*- coding: utf-8 -*-
"""
    Project:
    Purpose: 
    Version:
    Author:  ZG
    Date:    15/7/5
"""

from testLibrary.langconv import *


def f2j(line):
    # 转换繁体到简体
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    return line.encode('utf-8')

def j2f(line):
    # 转换简体到繁体
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    return line.encode('utf-8')

if __name__ == '__main__':

    f_line = """數百萬名希臘公民正在參加一項關鍵性的全民公決投票，以確定是否接受歐盟委員會、歐洲中央銀行和國際貨幣基金提出的解決希臘債務危機的金融拯救方案。
                全國各地的投票站已經在當地時間星期日（7月5日）早上7點（格林尼治標凖時間4點）開放，預料最初的結果會在當地時間當天晚間揭曉。
                公投票上寫出的問題是：「是否必須接受歐盟委員會、歐洲中央銀行和國際貨幣基金組織在2015年6月25日提交給歐元集團的協議計劃，以及構成其聯合建議的兩個文件？文件一：完成目前及後續計劃的改革；文件二：債務可持續性初步分析。」
                參加投票的選民必須在「接受」與「不接受」之間做出選擇。
                民意調查顯示，支持和反對接受國際拯救方案的選民人數旗鼓相當。
                調查同時顯示，參加這次公決的選民投票率將會比較高。
                希臘總理齊普拉斯在星期日投票後說，「沒有人能夠無視人民把命運掌握在自己手中的決心。」"""

    print f2j(f_line)
    print j2f("飞机飞向蓝天")