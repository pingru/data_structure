# encoding=utf8
"""
editor:lenovo
date:2022year03month10day
"""


# 实现选择排序select_sort

# 1.简单版本的选择排序的实现
# 长度为n的列表,遍历n次,每次选出列表中最小的元素,添加到一个新的列表里
def select_sort(lis):
    lis_new = []
    for i in range(len(lis)):
        val_min = min(lis)
        #     使用内置的min()取最小元素的函数 #def min(*args, key=None): # known special case of min
        # min(iterable, *[, default=obj, key=func]) -> value  #传参,传入可迭代对象,列表是可迭代对象
        # min(arg1, arg2, *args, *[, key=func]) -> value
        lis_new.append(val_min)  # 使用list.append()函数,将元素添加到列表中
        lis.remove(val_min)  # 使用list.remove(值)函数,将某值的元素从列表中删除<->list.pop(索引)函数,将某索引的元素从列表中删除
    return lis_new


lis = [3, 2, 4, 1, 5, 6, 8, 7, 9]


# print(select_sort(lis))

# 2.优化版本的选择排序
# 代码关键点是,有序区,无序区,最小数的位置
def select_sort_pro(lis):
    for i in range(len(lis) - 1):  # 遍历次数是列表长度减一
        min_loc = i
        for j in range((i + 1), len(lis)):
            if lis[j] < lis[min_loc]:
                lis[j], lis[min_loc] = lis[min_loc], lis[j]
        print(lis)


# 选择排序算法,不能加标志位change_flag,因为如果某一次选出来的元素比后面无序区所有元素值都小,那么无序区就不排了

lis = [3, 2, 4, 1, 5, 6, 8, 7, 9]
print(select_sort_pro(lis))
