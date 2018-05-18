# -*- coding:utf-8 -*-

import os
import sys

#sed.py 被替换内容 替换为
# 替换原文件中的某个字段,方法是新写一个文件
#print(sys.argc)
if not (1 < len(sys.argv) and len(sys.argv) <= 3):
    exit("argv err")

replace = sys.argv[1]
place = sys.argv[2]
print(replace,type(replace))

f = open('old.txt', 'r',encoding="utf-8")
f_new = open('new.txt', 'w',encoding="utf-8")
for line in f:
    if line.find(replace) != -1:
        newline = line.replace(replace,place)
        f_new.write(newline)
    else:
        f_new.write(line)
        print(line)
f.close()
f_new.close()
