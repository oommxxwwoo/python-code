__author__ = "Alex Li"

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        #a = b     a =1, b=2, a=b , a=2,
        # b = a +b b = 2+2 = 4
        n = n + 1
    return '---done---'

f= fib(10)
print(f)
#此处f只是一个内存地址
print(f.__next__())
#生成器 只有next一个方法，它只知道下一个什么

while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
