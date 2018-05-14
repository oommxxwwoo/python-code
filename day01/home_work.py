# -*- coding=utf-8 -*-

#登陆程序，从文件中读取用户名和密码，判断用户输入的用户名和密码是否正确，如果错误三次锁定
#文件格式如下
'''
root:root sh=/bin/bash false=0
user:user sh=/bin/bash false=0
'''

import os

#定义空字典， 存储 用户名和密码
LogMsg = {}

#定义空字典， 存储 用户名和登陆失败次数
LogFalseMsg = {}

#生成bk临时文件
#os.system("copy .\shadow .\shadow.bk")
print(os.popen("copy .\shadow .\shadow.bk").read())
#打开文件
f = open("shadow.bk","r",encoding="utf-8")
#循环遍历文件,将每一行文件内容，以:切片，增加字典内容
for line in f:
    line = line.strip()
    LogMsg[line[0:line.find(":")]] = line[line.find(":")+1 :line.find(" ")]
    LogFalseMsg[line[0:line.find(":")]] = int(line[line.find("false=") + 6: ])

f.close()

#打印字典
print(LogMsg, LogFalseMsg)
#打印字典key-value
for key in LogMsg:
    print(key,LogMsg[key])

err_cnt = 0
log_ok = 0
while True:
    #用户输入
    username = input("login:")
    password = input("password:")

    #遍历字典，查看用户登陆失败次数
    for key in LogFalseMsg:
        if username == key:
            err_cnt = LogFalseMsg[key]
            if(err_cnt >= 3):
                print("用户已锁定\n")
                break;

    if(err_cnt >= 3):
        break

    #遍历字典查找是否有对应的用户名和密码
    for key in LogMsg:
        if username == key and password == LogMsg[key]:
            print("welcom system , hello %s!" %username)
            log_ok = 1
            #清空失败次数
            LogFalseMsg[key] = 0
            break
    else:
        #遍历字典，更新登陆失败次数
        for key in LogMsg:
            if username == key:
                LogFalseMsg[key] += 1

        err_cnt += 1
        print("sorry! username or password erro, times = %s !!" %err_cnt)
        if(err_cnt >= 3):
            print("false to many times , break")
            break
        else:
            continue


    if(log_ok):
        break


print(LogMsg, LogFalseMsg)

#保存登陆信息

with open("shadow","w+") as fwrite , open("shadow.bk","r+") as fread:
    for line in fread:
        user =  line[0 : line.index(":")]
        if "false=" in line and user in LogFalseMsg:
            line_new = line[0 : line.index("false=")] + "false=%s\n"%LogFalseMsg[user]
            fwrite.write(line_new)




