# encoding=utf8
"""
editor:lenovo
date:2022year03month31day
"""
import random

'''
topk问题,是在一个无序列表中选取前k大的数,这种问题是非常常见的,尤其是当列表长度n比较大的时候,topk问题尤其需要被关注
解决方法1:先排序,再取前k大的数,可以用牛B三人组(快速排序,堆排序)的排序方法,时间复杂度O(nlogn)
解决方法2:用lowB三人组(冒泡排序,选择排序),只排k趟,时间复杂度O(nk)
解决方法3:用小根堆的堆排序方式进行,时间复杂度O(nlogk)
'''


# 解决方法3,用小根堆的堆排序方法,取得前k大的数的topk问题实现:
# 小根堆的,一次向下调整筛选函数实现:
def sift(lis, low, high):
    tmp = lis[low]
    i = low
    j = 2 * i + 1  # j是i的左孩子
    while j <= high:  # 在孩子节点不越界的前提下
        if j + 1 <= high and lis[j + 1] < lis[j]:  # 右孩子节点不越界,且右孩子更小
            j = j + 1  # j指向右孩子
        if lis[j] < tmp:  # 孩子节点比根节点小,把孩子节点提上去
            lis[i] = lis[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:
            break  # 当孩子节点都没有最初的那个根节点(tmp)小,退出循环
    lis[i] = tmp  # 孩子节点越界(即i遍历到叶子节点),或没有比tmp更小的孩子节点,将原根节点tmp赋值给当前遍历到的父节点,或叶子节点.


def topk(lis, k):
    # 创建一个节点数为k的二叉树,后面将这个二叉树,调整为小根堆
    heap = lis[0:k]
    # 1.创建小根堆
    for i in range((k - 2) // 2, -1, -1):  # 从最后一个非叶子节点开始调整
        sift(heap, i, k - 1)  # high=n-1是一个作弊操作,high只需要起到防止孩子节点越界的作用
    # 2.遍历原列表剩下的元素,进行对小根堆的调整
    for i in range(k, len(lis)):
        if lis[i] > heap[0]:  # 遇到比当前树根大的元素
            heap[0] = lis[i]  # 将树根元素舍弃,替换成遍历到的这个元素
            sift(heap, 0, k - 1)  # 小根堆筛选,将前k个元素中最小的元素提到根节点的位置
    # 3.挨个输出前k个最大的元素,还是要用棋子来顶掉根元素出来
    for i in range(k - 1, -1, -1):  # i指向当前堆的最后一个节点
        heap[0], heap[i] = heap[i], heap[0]  # 最后一个节点和根节点交换位置
        sift(heap, 0, i - 1)  # 在根节点和当前指向的最后一个节点的前一个节点之间用向下调整来进行筛选出,下一个最小的元素,这样前k个最大的数,输出出来就是降序的

    return heap


lis = list(range(50))
random.shuffle(lis)
print(lis)

print(topk(lis, 10))
