# -*- coding:utf-8 -*-

import datetime
import time

class getTimeDiff(object):
    def __init__(self, starttime, endtime):
        self.starttime = starttime
        self.endtime = endtime

    def TimeFormat(self):
        try:
            t1 = time.strptime(self.endtime, "%Y/%m/%d %H:%M:%S")
            t2 = time.strptime(self.starttime, "%Y/%m/%d %H:%M:%S")
        except ValueError as e:
            print("时间格式不正确：", e)
            quit()

        y, m, d, H, M, S = t1[0:6]
        global datetime_start
        datetime_start = datetime.datetime(y, m, d, H, M, S)
        y, m, d, H, M, S = t2[0:6]
        global datetime_end
        datetime_end = datetime.datetime(y, m, d, H, M, S)
        #判断时间大小
        if datetime_end > datetime_start:
            secDiff = (datetime_end - datetime_start).total_seconds()
            return secDiff
        else:
            secDiff = (datetime_start - datetime_end).total_seconds()
            return secDiff

    def monthDiff(self):
        months = abs((datetime_end.year - datetime_start.year) * 12 + (datetime_end.month - datetime_start.month) * 1)
        return months


if __name__ == "__main__":
    endate = input(u"请输入结束时间：")
    startdate = input(u"请输入开始时间：")
    results = getTimeDiff(startdate, endate).TimeFormat()
    minDiff = results/60
    dayDiff = results/(3600*24)
    monthDiff = getTimeDiff(startdate, endate).monthDiff()
    print("相差秒数：", results)
    print("相差分钟数：", minDiff)
    print("相差天数：", '%.2f'%dayDiff)
    print("相差月份数", monthDiff)
