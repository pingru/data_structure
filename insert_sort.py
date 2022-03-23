# encoding=utf8
"""
editor:lenovo
date:2022year03month21day
"""


# 实现插入排序算法insert_sort
def insert_sort(lis):
    for i in range(1, len(lis)):  # i代表抽到牌的下标,从第二个元素遍历到最后一个元素,i是下标
        tmp = lis[i]  # 将抽到的牌的值保存在暂存值tmp变量里
        j = i - 1  # j是被抽到牌的前一个元素的下标,将从前一个元素一直向前遍历
        while j >= 0 and lis[j] > tmp: #这里一定要用tmp比,因为下面会将lis[i]位置的值替换掉,因此这个待比较的值也会被更新掉,因此要用tmp常量变量
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = tmp


lis = [3, 2, 4, 1, 5, 7, 9, 6, 8]
insert_sort(lis)
print(lis)
