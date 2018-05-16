# -*- coding:utf-8 -*-
# Auth: mxw

#定义空列表
login_list = []

def loadLoginMsg():
    #清除列表所有元素；除字符串，单元素变量外，若要修改全局变量需要加入global关键字声明；
    # [列表/字典/元组/集合等具有全局变量作用域]
    login_list.clear()#清除列表缓存
    with open("login.log", "r", encoding="utf-8") as f:
        for line in f:
            login_tmp = []
            login_tmp = line.strip().split(',')#以逗号作为分割符将字符串转为列表
            login_tmp[2] = int(login_tmp[2])
            login_list.append(login_tmp)#向login_list列表追加元素


loadLoginMsg()
print(login_list)

err_cnt = 0
log_ok = 0

while True:
    username = input("username:")
    password = input("password:")
    err_cnt += 1
    #遍历俩儿表查找对应用户名密码
    for i in range(len(login_list)):
        if username == login_list[i][0] and password == login_list[i][1] and login_list[i][2] <= 3:
            login_list[i][2] = 0
            print("welcom {_username} to this system !!!".format(_username = username))
            log_ok = 1
            err_cnt = 0
            break
        else:
            if username == login_list[i][0]:
                login_list[i][2] += 1
                print("username or password erro,,times = %s " %login_list[i][2])
            else:
                if i < (len(login_list) - 1):
                    continue

    if log_ok or err_cnt >= 3 or login_list[i][2] > 3:
        print("erro to many times >= 3, locked!!!")
        err_cnt = 0
        break
'''
login.log文件格式：
root,123456,0
user,123,1
'''
#保存的登陆log信息
with open("login.log","w+",encoding="utf-8") as fwrite:
    for i in range(len(login_list)):
        login_list[i][2] = str(login_list[i][2])#将列表中的数字转换为字符串
        line = " ".join(login_list[i])#将列表转换为字符串
        line = line.replace(' ', ',') + '\n'#替换空格为逗号，并换行
        fwrite.write(line)


