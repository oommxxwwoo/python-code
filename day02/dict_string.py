#字典转字符串
a = {'a' : 1, 'b' : 2, 'c' : 3}
b = str(a)
print(type(b),b)
#字符串转字典
a = "{'a' : 1, 'b' : 2, 'c' : 3}"
b = eval(a)
print(type(b),b)


#字符串转为元组，返回：(1, 2, 3)
print(eval("(1,2,3)"))
print( tuple(eval("(1,2,3)")))
#字符串转为列表，返回：[1, 2, 3]
print(list(eval("(1,2,3)")))
#字符串转为字典，返回：<type 'dict'>
print(type(eval("{'name':'ljq', 'age':24}")))