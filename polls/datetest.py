import calendar
import functools
import time

# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)
#
# # 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# cal=calendar.month(2019,11)
# print(cal)


# 作用于任何函数上，并打印该函数的执行时间.具体怎么用不知道
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kw):
#         time0=time.time()
#         ret=fn(*args,**kw)
#         time1=time.time()
#         print('%s executed in ms '% (fn.__name__,time1-time0))
#         return ret
#     return wrapper()

