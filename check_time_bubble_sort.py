# encoding=utf8
"""
editor:lenovo
date:2022year03month23day
"""
from time_check import *
import random


@cal_time
def bubble_sort2(lis):
    for i in range(len(lis) - 1):
        exchange = False
        for j in range(len(lis) - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                exchange = True
        if exchange == False:
            return


li = list(range(10000))  # 创建1万个顺序数字元素的列表
random.shuffle(li)  # random模块的shuffle函数,将列表洗牌打乱
bubble_sort2(li)  # 使用优化后的冒泡排序bubble_sort函数,将列表排序
# 跑的结果是9.207552671432495 secs
# 可以估算结果,一般普通电脑1秒可以处理10^7位,那么时间复杂度是O(n^2)的程序,10^4^2=10^8,因此大概是10秒的处理时间
