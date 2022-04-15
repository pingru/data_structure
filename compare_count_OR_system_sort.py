# encoding=utf8
"""
editor:lenovo
date:2022year04month15day
"""
'''
sort()是系统排序函数,用C语言写的,拿它跟count_sort()计数排序对比运算时间的差别:
有些时候,count_sort()比sort()更快,虽然我语言比你慢,但是我算法比你快
但是我电脑测的时候,实际上还是system_sort要更快一点
'''
from time_check import *

# 这里不能只写import time_check 这样调用装饰器函数cal_time的时候,还得把模块名写在前面,不符合规则,所以,需要将装饰器定义的模块的全部内容引入,而不是仅引入模块名

@cal_time
def count_sort(lis, max_count=100):  # 排序的列表的数据范围,最大是100
    count = [0 for i in range(max_count + 1)]
    # 因为数据范围是0-100,所以是101个数长度的列表,并且该列表初始化每个位置的元素都是0
    for val in lis:  # 遍历列表中的每一个元素值val
        count[val] += 1  # 在列表下标为val的位置进行叠加累计元素val出现的次数
    lis.clear()  # 用list.clear()函数将原列表空间删光
    for id, val in enumerate(count):  # 按照count列表的顺序下标位置进行遍历
        for i in range(val):  # 针对顺序下标位置的每一个元素值,按照元素值记录,进行对该位置下标值的复制跟接append
            lis.append(id)


@cal_time
def sys_sort(lis):  # 用一个新的函数定义包一下,系统内自带的sort()列表排序函数,以便,在函数定义处使用装饰器来进行函数运行时间的统计功能
    lis.sort()


import random, copy

lis = [random.randint(0, 100) for i in range(1000000)]  # 创建长度为100万的列表,每个元素是数值范围0-100内,随机生成的整数
lis1 = copy.deepcopy(lis)  # copy模块的深拷贝deepcopy生成一个新的列表,完全从原列表中取得元素信息(只有浅拷贝会带来数据安全的隐患!!)
lis2 = copy.deepcopy(lis)
count_sort(lis1)
sys_sort(lis2)
