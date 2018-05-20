# -*- coding:utf-8 -*-

import time

'''
#装饰器

一 : 函数即变量
二 : 高阶函数--返回函数/调用函数


不改变函数代码
不改变原有函数的调用关系
'''
def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time is %s "%(stop_time - start_time))
    return deco

@timer  #test1=timer(test1),充分体现了函数即变量的思想
def test1():
    time.sleep(2)
    print("in the test1")

@timer  #test2=timer(test2) [最外层参数]   +   deco (str) 【内层参数]
def test2(str):
    time.sleep(3)
    print("in the test2,hi %s" %str)



test1()
test2("menxiuwei")