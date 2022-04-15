# 比较线性查找和二分查找的时间复杂度(运行时间)的差别

from time_check import *


@cal_time
def linear_search(lis, val):
    for id, v in enumerate(lis):
        if v == val:
            return id
    else:
        return None


@cal_time
def binary_search(lis, val):
    left = 0
    right = len(lis) - 1
    # ** mid值是要一直更新的,不能放在循环外面
    # mid = (left+right) // 2
    while left <= right:
        # ** mid索引要一直更新位置,需要放在循环内部
        # 下面没找到的时候,left索引或right索引也在一直更改位置,放在循环内有更新
        mid = (left + right) // 2
        if lis[mid] == val:
            return mid
        elif lis[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


# print(list(range(10))) #快速创建一个具有顺序的列表
lis = list(range(10000000))
check = 3890000
print(linear_search(lis, check))
print(binary_search(lis, check))
