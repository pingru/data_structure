# encoding=utf8
"""
editor:lenovo
date:2022year03month31day
"""
import random


# 归并过程的实现
def merge(lis, low, mid, high):
    i = low  # i先指向列表最左边
    j = mid + 1  # j先指向右边有序区列表的第一个位置
    ltmp = []  # ltmp临时列表用于存储
    while i <= mid and j <= high:  # 在左右有序区内都有数的前提下
        if lis[i] < lis[j]:  # 如果左边有序区的小数比右边有序区的小数小
            ltmp.append(lis[i])  # 把较小的那个数,拿出来存到临时列表里
            i += 1  # 左边区域指针指向下一个位置
        else:
            ltmp.append(lis[j])  # 如果是右边有序区的元素比较小的话,将右边小数存起来
            j += 1  # 右边区域指针指向下一个位置
    # while执行完,肯定是有一部分区域没有数了,那么把剩下一部分的区域内的全部元素都取出,直接送入临时列表中
    while i <= mid:  # 证明左边区域还有数
        ltmp.append(lis[i])
        i += 1
        # 将左边区域内的元素,一个一个append进去
    while j <= high:
        ltmp.append(lis[j])
        j += 1
    lis[low:high + 1] = ltmp  # 将排好序的临时列表来替换掉原来的列表


# lis = [2,4,5,7,1,3,6,8]  #左边部分的2,4,5,7是有序的,同时右边部分1,3,6,8也是有序的
# merge(lis,0,3,7) #将low,mid,high的下标位置提供给merge函数
# print(lis)

# 归并排序的实现
def merge_sort(lis, low, high):
    if low < high:  # 两个指针区间内至少有2个元素
        mid = (low + high) // 2
        merge_sort(lis, low, mid)  # 把列表左边部分排好序
        merge_sort(lis, mid + 1, high)  # 把列表右边部分排好序
        # print(lis[low:high+1])
        merge(lis, low, mid, high)  # 两边都是有序的话,归并一次就可以了
        # print(lis[low:high+1])


lis = list(range(10))
random.shuffle(lis)
print(lis)
merge_sort(lis, 0, len(lis) - 1)  # high指向最后一个位置的下标
print(lis)
