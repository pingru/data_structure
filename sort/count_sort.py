# encoding=utf8
"""
editor:lenovo
date:2022year04month15day
"""
'''
count sort是计数排序,前提是知道我要排序的列表的数据的取值范围,时间复杂度最低,是O(n)
1 3 2 4 1 2 3 1 3 5
另外创建一个列表(不用存储的顺序下标,就是其保存的数据范围信息):
lis:
下标 值
0   0
1   3
2   2
3   3
4   1
5   1
再按照存储的列表内值的信息,顺序输出对应数量的下标值来:
1 1 1 2 2 3 3 3 4 5
'''


def count_sort(lis, max_count=100):  # 排序的列表的数据范围,最大是100
    count = [0 for i in range(max_count + 1)]
    # 因为数据范围是0-100,所以是101个数长度的列表,并且该列表初始化每个位置的元素都是0
    for val in lis:  # 遍历列表中的每一个元素值val
        count[val] += 1  # 在列表下标为val的位置进行叠加累计元素val出现的次数
    lis.clear()  # 用list.clear()函数将原列表空间删光
    for id, val in enumerate(count):  # 按照count列表的顺序下标位置进行遍历
        for i in range(val):  # 针对顺序下标位置的每一个元素值,按照元素值记录,进行对该位置下标值的复制跟接append
            lis.append(id)


import random

lis = [random.randint(0, 100) for i in range(1000)]  # 生成长度是1000的列表,其中每个元素是随机的0,100数值范围的随机整数
print(lis)
count_sort(lis)
print(lis)
