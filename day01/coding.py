#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auth:mxw

for i in range(1,10): #for i in range(1,10,2):
    if i < 3:
        print("i = ", i)
    else:
        if i == 5 :
            print("i = ", i)
            break
        else:
            continue
    print("print")

msg="12345678"


print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))

