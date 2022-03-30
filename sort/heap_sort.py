# encoding=utf8
"""
editor:lenovo
date:2022year03month30day
"""
#heap是堆的意思，heap_sort是牛B三人组的第二个，堆排序
#sift是筛选的意思，这是一次向下调整过程，也是筛选出最大根候选的过程
#sift的前提是，认为这是一个除了根节点外，左右子树是大根堆的情况（即除了根节点外，左右子树都是有秩序的）
def sift(lis,low,high):  #树用顺序存储方式，即用列表存储，low是树根，high是最后一个节点
    tmp = lis[low] #保存根节点值
    i = low
    j = 2 * low + 1 #j是i的左孩子节点下标
    while j <= high: #孩子节点还没越界
        if j+1 <= high and lis[j+1] > lis[j]:  #先判断两个孩子节点，哪个大，j要指向较大的那个孩子节点
            j = j+1
        if lis[j] > tmp:
            lis[i] = lis[j]
        else:
            break
    lis[i] = tmp

