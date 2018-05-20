__author__ = "Alex Li"

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield#遇到yield 就会return __line__，相当于返回当前函数的行号，只有在下一次调用时，才从此行号处继续执行，遇到yield再次返回行号，以此类推

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

c = consumer("ChenRonghua")
#c.__next__()
#c.__next__()
#
# c.__next__()
# b1= "韭菜馅"
# c.send(b1)

def producer():
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)
        c2.send(i)

producer()