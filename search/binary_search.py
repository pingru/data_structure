# 列表查找 方法2
# binary search 二分查找 即 折半查找
# 排好序(从小到大排序)之后,待查找区域的中间值与待查找元素值进行比较
def binary_search(lis, val):
    # 创建两个'指针'并初始化 (python这里的指针都是列表list的索引)
    # 左指针指向列表的第一个索引
    # 右指针指向列表的最后一个索引,即列表长度减1
    lef = 0
    rig = len(lis) - 1
    # 要保证待查找区域内有值,那么left指针不能在right指针的右边
    while lef <= rig:
        mid = (lef + rig) // 2
        if lis[mid] == val:  # 待查找的值刚好是中间值,返回索引
            return mid
        elif lis[mid] > val:  # 待查找值在中间值的 左边
            rig = mid - 1
        else:  # 待查找值在中间值的 右边
            lef = mid + 1
    else:
        return None


lis_test = [1, 2, 3, 4, 5]
# lis_test = [2,5,1,4,6] #未排序的列表是不能用上面的函数直接进行查找的,会有bug: val =2 ,5 都返回None找不到
val = 2
print(binary_search(lis_test, val))
