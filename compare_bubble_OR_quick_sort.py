# encoding=utf8
"""
editor:lenovo
date:2022year03month25day
"""
# 这个文件用来比较冒泡排序bubble_sort和快速排序quick_sort运行时间之间的区别

from time_check import *  # 调用运行时间测试的装饰器
import random
import copy  # 引用copy模块,为了调用深拷贝函数


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


def partition(lis, left, right):
    tmp = lis[left]
    while left < right:  # 分区内至少有2个元素
        while left < right and lis[right] >= tmp:  # 分区内至少有两个元素,并且右边元素大于要放在中间的值
            right -= 1  # 右边指针向左移一个
        lis[left] = lis[right]  # 右边的小值,送到左边的空位
        while left < right and lis[left] <= tmp:  # 分区内至少有两个元素,并且左边元素小于要放在中间的值
            left += 1  # 左边指针向右移一个
        lis[right] = lis[left]  # 左边大值,更新到右边的小值处
    lis[left] = tmp  # left=right的时候,将中间值赋到中间位置
    return left


def _quick_sort(lis, left, right):  # 递归算法,递归1.调用自身,2.结束条件
    # 一定要检查有没有'结束条件的判断'
    if left < right:
        mid = partition(lis, left, right)
        _quick_sort(lis, left, mid - 1)
        _quick_sort(lis, mid + 1, right)


@cal_time
def quick_sort(lis):  # 递归函数测试运行时间的时候,使用这种套一个马甲的方式进行装饰器的调用,如果装饰器直接加在递归函数的前面,它会打印很多次运行时间
    _quick_sort(lis, 0, len(lis) - 1)  # 这里注意,right传入的是最右边元素的下标,一定要len(lis)-1,一定要减一,总错!


lis = list(range(10000))
random.shuffle(lis)

lis1 = copy.deepcopy(lis)
lis2 = copy.deepcopy(lis)

quick_sort(lis1)
bubble_sort2(lis2)
