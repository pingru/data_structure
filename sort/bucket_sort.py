# encoding=utf8
"""
editor:lenovo
date:2022year04month19day
"""


def bucket_sort(lis, n=100, max_num=10000):
    # n是桶的个数,给默认值100,max_num是数据范围,给默认值最大到10000
    buckets = [[] for _ in range(n)]  # 创建桶集,一共创建n个桶
    for var in lis:
        i = min(var // (max_num // n), n - 1)
        # i表示var元素放到几号桶里,min()是防止10000//100 = 100,但是数10000只有一个数,应当放在第99号桶里
        # 10000//100 == max_num//n 数据范围除以桶的个数,得到桶的长度(大小)
        # var//(max_num//n) == var//桶的大小,得到当前元素应当放在第几个桶里,从0号桶开始
        buckets[i].append(var)  # 把var元素存到它隶属于的第i个桶内

        # 下面是使每一个桶,都保持顺序:从小到大:
        for j in range(len(buckets[i]) - 1, 0, -1):
            # 从每个桶的最后一个元素往前遍历,到从前往后数第二个元素截止
            if buckets[i][j] < buckets[i][j - 1]:  # 把小的元素交换到前面去
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
                # 如果发现前面的数已经比当前的数小了,那么当前的位置就是正确的,这个前面比它小的数,再向前只有比它更小的数,不需要再比较
                # 原来的列表是这样的:[-1, 0, 3, 4];当2来了之后,向前交换移动,到0的后面,即停止即可:[-1,0,2,3,4]--ok

    sorted_lis = []  # 处理完的列表用这个变量接收
    for buc in buckets:
        sorted_lis.extend(buc)
        # 用+这个符号也可以,用extend函数也可以,extend直接将其他列表添加在当前列表的后面
    return sorted_lis


import random

lis = [random.randint(0, 10000) for _ in range(100000)]  # 数据范围是0-10000,随机生成100000个数
print(bucket_sort(lis))  # 函数的返回值是排好序的列表,原列表空间不进行改动
