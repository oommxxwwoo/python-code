# -*- coding:utf-8 -*-

str = "hi hellow world"

list = str.split(' ')#字符串以空格为间隔转换为列表
print(list)

#['hi', 'hellow', 'world']

list1 = ['hi', 'hellow', 'world']
str1 = ' '.join(list1)#列表转换为字符串
print(str1)

#hi hellow world
