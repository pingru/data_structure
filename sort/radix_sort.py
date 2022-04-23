# encoding=utf8
"""
editor:lenovo
date:2022year04month23day
"""
'''
基数排序,radix是根root的意思,基数
'''
from time_check import *


@cal_time
def radix_sort(lis):
    max_num = max(lis)
    # 查看列表中元素的最大值 最大值和循环次数,基数位数有关 9->1, 99-2,999->3,1000->4
    it = 0  # it是iteration迭代的简写
    while 10 ** it <= max_num:
        # 当it是3时,10^3 = max_num=1000,要继续循环将迭代次数变为4,it+1=3+1=4
        # 每一次迭代中,要按照列表lis中所有元素的每一位的数字进行装桶
        buckets = [[] for _ in range(10)]  # 一共有10个桶,代表数字0-9
        for var in lis:
            # 987
            # it=0: 987//1->987%10=7;
            # it=1: 987//10->98%10=8;
            # it=2: 987//100->9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
            # 按照当前迭代中,列表lis每一个元素的这一位的数字进行按桶存储
        # 对于这一次迭代,元素们分桶完成
        lis.clear()
        # 清空源列表空间
        for buc in buckets:
            lis.extend(buc)
            # 按照这一次迭代所研究的位置进行装桶的顺序,存回源列表中

        it += 1
        # 迭代标识数更新,准备开启下一轮迭代,关注下一位数(下一位基数)


def partition(lis, left, right):
    tmp = lis[left]
    while left < right:  # 分区内至少有2个元素
        while left < right and lis[right] >= tmp:  # 分区内至少有两个元素,并且右边元素大于要放在中间的值
            right -= 1  # 右边指针向左移一个
        lis[left] = lis[right]  # 右边的小值,送到左边的空位
        # print(lis, 'right')
        while left < right and lis[left] <= tmp:  # 分区内至少有两个元素,并且左边元素小于要放在中间的值
            left += 1  # 左边指针向右移一个
        lis[right] = lis[left]  # 左边大值,更新到右边的小值处
        # print(lis, 'left')
    lis[left] = tmp  # left=right的时候,将中间值赋到中间位置
    return left


def quick_sort(lis, left, right):  # 递归算法,递归1.调用自身,2.结束条件
    # 一定要检查有没有'结束条件的判断'
    if left < right:
        mid = partition(lis, left, right)
        quick_sort(lis, left, mid - 1)
        # print(lis, '左')
        quick_sort(lis, mid + 1, right)
        # print(lis, '右')


@cal_time
def quick_sort_wrap(lis):
    quick_sort(lis, 0, len(lis) - 1)
# 注意递归函数的运行时间计时,要定义一个函数,这个函数调用原递归函数

import random
import copy

lis = list(range(1000))
random.shuffle(lis)
lis1 = copy.deepcopy(lis)
lis2 = copy.deepcopy(lis)

radix_sort(lis1)
quick_sort_wrap(lis2)
# 运行结果可以看到,基数排序甚至更快一点
