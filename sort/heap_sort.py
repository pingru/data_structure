# encoding=utf8
"""
editor:lenovo
date:2022year03month30day
"""

import random


# heap是堆的意思，heap_sort是牛B三人组的第二个，堆排序
# sift是筛选的意思，这是一次向下调整过程，也是筛选出最大根候选的过程
# sift的前提是，认为这是一个除了根节点外，左右子树是大根堆的情况（即除了根节点外，左右子树都是有秩序的）
def sift(lis, low, high):  # 树用顺序存储方式，即用列表存储，low是树根，high是最后一个节点
    tmp = lis[low]  # 保存根节点值
    i = low
    j = 2 * i + 1  # j是i的左孩子节点下标
    while j <= high:  # 孩子节点还没越界
        if j + 1 <= high and lis[j + 1] > lis[j]:  # 先判断两个孩子节点，哪个大，j要指向较大的那个孩子节点
            j = j + 1
        if lis[j] > tmp:
            lis[i] = lis[j]
            i = j  # 要往下看一层
            j = 2 * i + 1
        else:
            break
    lis[i] = tmp


def heap_sort(lis):
    n = len(lis)
    # 创建堆
    for i in range((n - 2) // 2, -1, -1):
        sift(lis, i, n - 1)  # high传n-1，因为不越界就行
    # 一个一个出数
    for i in range(n - 1, -1, -1):
        lis[0], lis[i] = lis[i], lis[0]  # 先把每次完整堆的最大值（最大根）取出来,并把最后一个元素节点放到根处
        sift(lis, 0, i - 1)  # high是当前最后一个节点的前一个节点位置，当前最后一个节点是i指向的


lis = list(range(10))
random.shuffle(lis)
print(lis)
heap_sort(lis)
print(lis)

# 堆排序在python语言中有内置模块
import heapq
import random

li = list(range(50))
random.shuffle(li)
print(li)
# 创建堆 创建的是小根堆
heapq.heapify(li)
print(li)
res = []
for i in range(len(li)):
    a = heapq.heappop(li)
    print(a, end=',')
    res.append(a)
print()
print('保存结果是')
print(res)
