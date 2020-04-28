# -*- coding:utf-8 -*-

import datetime
import time

def getTimeDiff(endtime, starttime):
    t1 = time.strptime(endtime, "%Y/%m/%d %H:%M:%S")
    t2 = time.strptime(starttime, "%Y/%m/%d %H:%M:%S")
    y, m, d, H, M, S = t1[0:6]
    datetime_start = datetime.datetime(y, m, d, H, M, S)
    y, m, d, H, M, S = t2[0:6]
    datetime_end = datetime.datetime(y, m, d, H, M, S)
    if datetime_end > datetime_start:
        secDiff = (datetime_end - datetime_start).total_seconds()
        return secDiff
    else:
        secDiff = (datetime_start - datetime_end).total_seconds()
        return secDiff
'''
def dayDiff(datetime_end, datetime_start):
    days = (datetime_end - datetime_start).days
    return dayDiff
def secDiff(datetime_end, datetime_start):
    secDiff = (datetime_end - datetime_start).total_seconds()
    return secDiff
def minDiff(dayDiff, secDiff):
    minDiff = dayDiff*1440 + round(secDiff/60, 1)
    return minDiff'''

if __name__ == "__main__":
    endate = input(u"请输入结束时间：")
    startdate = input(u"请输入开始时间：")
    minDiff = getTimeDiff(endate, startdate)/60
    dayDiff = getTimeDiff(endate, startdate)/(3600*24)
    print("相差秒数：", getTimeDiff(endate, startdate))
    print("相差分钟数：", minDiff)
    print("相差天数：", '%.2f'%dayDiff)
