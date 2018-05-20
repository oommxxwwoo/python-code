# __author__ = "Alex Li"

print( all([1,-5,3]) )
#all判断对象元素是否有非真元素,只要有非真的元素，则为false
print( any([1, 0]) )
#只要有 为真 的元素，则为true


a= ascii([1,2,"开外挂开外挂"])
print(type(a),[a])
#可打印形式

a = bytes("abcde",encoding="utf-8")
b = bytearray("abcde",encoding="utf-8")
#可修改的二进制数组。。。默认：字符串是不能修改的
print( b[1] )
b[1]= 50
print(b)


a = "abx"
print(a.capitalize(),a)
#copy+首字符大写
def sayhi():pass
print( callable(sayhi) )
#是否可被调用

# code = '''
# def fib(max): #10
#     n, a, b = 0, 0, 1
#     while n < max: #n<10
#         #print(b)
#         yield b
#         a, b = b, a + b
#         #a = b     a =1, b=2, a=b , a=2,
#         # b = a +b b = 2+2 = 4
#         n = n + 1
#     return '---done---'
#
# #f= fib(10)
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
#
# '''
#
# #py_obj = compile(code,"err.log","exec")
# #exec(py_obj)
#
# #exec(code)
#
#
# # def sayhi(n):
# #     print(n)
# #     for i in range(n):
# #         print(i)
# # sayhi(3)
# #
# # #(lambda n:print(n))(5)
# # calc = lambda n:3 if n<4 else n
# # print(calc(2))
#
res = filter(lambda n:n>5,range(10))#生成器
print(res )
for i in res:
    print(i)
res = map(lambda n:n*2,range(10))#生成器
print(res )
res = [ lambda i:i*2 for i in range(10)]#生成器
print(res )
import functools
res = functools.reduce( lambda x,y:x*y,range(1,10 ))
print(res )

a = frozenset([1,4,333,212,33,33,12,4])
#不可改变的集合，被冻结的

print(globals())
#获得本程序（文件）的所有变量及value
print(globals().get(a))#获取a 变量的 值 ；get不存在的key，会报错

# def test():
#     local_var =333
#     print(locals())
#     print(globals())
# test()
# print(globals())
# print(globals().get('local_var'))


a = {6:2,8:0,1:4,-5:6,99:11,4:22}
#sorted排序
print(  sorted(a.items()) )
print(  sorted(a.items(),key=lambda x:x[1]) )
print(a )

a = [1,2,3,4,5,6]
b = ['a','b','c','d']

print(zip(a,b))# 生成器

for i in zip(a,b):
    print(i)
#zip 拉链的意思

#import 'decorator'
#__import__('decorator')
