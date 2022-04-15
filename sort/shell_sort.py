# encoding=utf8
"""
editor:lenovo
date:2022year04month10day
"""


# 这段就是插入排序,但是将间隔1变成了间隔gap,也就是每次忽略gap中间的那些数,但是不同组之间的快速是一次同时进行的
def insert_sort_gap(lis, gap):  # 这一段的实现就是插入排序,但是把1替换成gap就可以了
    for i in range(gap, len(lis)):  # i是摸到的牌的下标,从列表的第gap位开始抽(也就是每次隔gap个位置抽牌)
        tmp = lis[i]  # 将抽到的牌暂时保存在tmp变量上
        j = i - gap  # j指的是手里的牌的下标 #通过i的循环和每次减gap的结合,可以按照间隔gap的每组的形式把几组分别进行插入排序
        while j >= 0 and lis[j] > tmp:  # j是向前推位置的,当j不超出列表头;j位置的元素比抽到牌位置的元素大:
            lis[j + gap] = lis[j]  # 把大的牌替换到后面去(抽到牌的位置)
            j -= gap  # 按照隔gap个位置的方式,向前推进,指针位置移动到最前面待查位置
        lis[j + gap] = tmp  # 把抽到的牌放在它该放的位置上


def shell_sort(lis):
    d = len(lis) // 2  # 先按照列表长度一半,进行gap,组宽的初始化
    while d >= 1:  # 循环到d为1截止
        insert_sort_gap(lis, d)
        d //= 2  # d每次更新的时候,截半更新


lis = list(range(1000))
import random

random.shuffle(lis)
shell_sort(lis)
print(lis)
