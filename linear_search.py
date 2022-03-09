#列表查找 方法1
#linear search 顺序查找 即 线性查找
#从第一个元素一个一个向后查找,直到找到最后一个.
# 找到要找元素,返回索引index值;没有找到元素,则返回None或-1
#创建线性查找函数,要传入待查找的列表,和要找的元素
def linear_search(lis,val):
    for ind,v in enumerate(lis):
        if v == val:
            return ind
    else:
        return None
    
lis_test = [1,2,3,4,5]
val = 6
print(linear_search(lis_test,val))