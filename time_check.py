#这个模块内创建的函数,用来测试其他函数的运行时间
#使用时,将此函数作为装饰器,装饰在要被测试的函数的定义之前
import time

#calculate time 是一个装饰器函数
#装饰器函数,传入参数是被装饰函数,返回值是装饰出来的新函数
#装饰器函数,需要传参的时候,使用闭包结构
def cal_time(func):
    def wrapper(*args,**kargs): #一个*传入的是未命名不定长变量参数(数组),两个**传入的是命名不定长变量参数(字典)
        #记录时刻1,time模块下的time()函数可以记录该时间点
        t1 = time.time()
        #执行原函数,函数的传参,我们不确定,所以用两种类型的不定长参数接收
        result = func(*args,**kargs)
        #记录时刻2,time模块下的time()函数可以记录该时间点
        t2 = time.time()
        #返回原函数,保留函数的返回值状态
        #**
        #要将运行时间打印出来
        print('%s running time: %s secs.'%(func.__name__,t2-t1))
        return result
    #装饰原函数,原函数执行的时候,其实在执行wrapper(*args,**kargs)函数,该传入的不定长参数按需传入
    return wrapper