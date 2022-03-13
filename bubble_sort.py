# encoding=utf8
"""
editor:lenovo
date:2022year03month10day
"""
# 实现冒泡排序
# 冒泡排序就像烧开了的开水,大的泡泡因为含有气体多,会上升,那么把列表竖过来,大索引在上,数值大的数,就会被提升到上面去
# 在排序过程中,会自然形成有序区和无序区
# 编程的关键是:1)排序趟数;2)分清哪里是有序区,哪里是无序区

# for ... in range(..)的好处就是,rang(..)里面可以直接写你要拍的次数,因为从0开始,包左,不包右,是正好保证i能提供你range(..)里要求的次数
# 所以就可以不需要中间转化思维过程了,你要几,就直接写几就行,从1开始算

import random


def bubble_sort(lis):
    for i in range(len(lis) - 1):  # 排序的趟数,一共会排len(list)-1趟
        for j in range(len(lis) - i - 1):  # 每次无序区的范围,其实是len(lis)-i-1
            # j代表虚拟的指针箭头
            if lis[j] > lis[j + 1]:  # 降序排序的话,将大于号变成小于号就可以
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                # 这是交换两个元素的快速写法,注意一下
                # 当前面的比后面的大,交换两个元素


lis = [random.randint(0, 10000) for i in range(1000)]
#    def randint(self, a, b):   #random.randint() random模块里的randint()函数产生从a到b的整数,可包括a和b
#         """Return random integer in range [a, b], including both end points.
#         """   #randint(self, a, b)函数传参的形式注意
print('对长度为1000的随机列表进行升序排序')
print(lis)
bubble_sort(lis)
print(lis)


###############################################
# 降序每趟的迭代情况演示:
def bubble_sort1(lis):
    for i in range(len(lis) - 1):  # 排序的趟数,一共会排len(list)-1趟
        for j in range(len(lis) - i - 1):  # 每次无序区的范围,其实是len(lis)-i-1
            # j代表虚拟的指针箭头
            if lis[j] < lis[j + 1]:  # 降序排序的话,将大于号变成小于号就可以
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
        print(i, lis)  # 把每一趟排好的,迭代打印出来


print('对lis1排序')
lis1 = [3, 2, 4, 6, 5, 1, 8, 7, 9]
print(lis1)
bubble_sort1(lis1)
# 打印结果能看到有序区的向左延伸过程
# 当一趟排序中,没有进行任何交换,那么就可以认为排序已经完成:
print('对lis2排序')
lis2 = [9, 8, 7, 6, 5, 1, 2, 3, 4]
print(lis2)
bubble_sort1(lis2)


##################### bubble_sort()函数改进 ##############
##############根据前面显示出的bug,在每一趟排序中添加一个标志位##############
def bubble_sort2(lis):
    for i in range(len(lis) - 1):
        exchange = False
        for j in range(len(lis) - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                exchange = True
        print(i, lis)
        if exchange == False:
            return


lis2 = [9, 8, 7, 6, 5, 1, 2, 3, 4]
print('对lis2进行排序(修正代码)')
print(lis2)
bubble_sort2(lis2)
lis3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('对lis3进行排序(修正代码)')
print(lis3)
bubble_sort2(lis3)
