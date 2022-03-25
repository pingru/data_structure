# encoding=utf8
"""
editor:lenovo
date:2022year03month25day
"""


def partition(lis, left, right):
    tmp = lis[left]
    while left < right:  # 分区内至少有2个元素
        while left < right and lis[right] >= tmp:  # 分区内至少有两个元素,并且右边元素大于要放在中间的值
            right -= 1  # 右边指针向左移一个
        lis[left] = lis[right]  # 右边的小值,送到左边的空位
        print(lis, 'right')
        while left < right and lis[left] <= tmp:  # 分区内至少有两个元素,并且左边元素小于要放在中间的值
            left += 1  # 左边指针向右移一个
        lis[right] = lis[left]  # 左边大值,更新到右边的小值处
        print(lis, 'left')
    lis[left] = tmp  # left=right的时候,将中间值赋到中间位置
    return left


def quick_sort(lis, left, right):  # 递归算法,递归1.调用自身,2.结束条件
    # 一定要检查有没有'结束条件的判断'
    if left < right:
        mid = partition(lis, left, right)
        quick_sort(lis, left, mid - 1)
        print(lis, '左')
        quick_sort(lis, mid + 1, right)
        print(lis, '右')


lis = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(lis, 0, len(lis) - 1)
print(lis, '终')
