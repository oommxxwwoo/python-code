#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auth: mxw

import json
import os

def fetch(backend):
    backend_title = 'backend %s' % backend #字符串组合
    record_list = []
    with open('ha') as obj:
        flag = 0
        for line in obj:
            line = line.strip()
            if line == backend_title and  line.startswith('backend'):
                flag = 1
                continue
            if flag and line and not line.startswith("backend"):
                record_list.append(line)
                break
            else:
                if flag:
                    break

    return record_list


def add(dict_info):
    backend = dict_info.get('backend')#获取key的值
    record_list = fetch(backend)#查找value
    backend_title = "backend %s" % backend#字符串组合，生成标题
    current_record = "server %s %s weight %d maxconn %d" % (
    dict_info['record']['server'], dict_info['record']['server'], dict_info['record']['weight'],
    dict_info['record']['maxconn'])#当前的数据

    record_list.append(current_record)#将当前数据放入列表，准备写入

    with open('ha','r+',encoding="utf-8") as read_file, open('ha.new', 'w+',encoding="utf-8") as write_file:
        flag = False
        for line in read_file:
            print(line)
            if line.strip() == backend_title: #找到标题处
                write_file.write(backend_title +'\n')#写入标题及内容
                if record_list:#如果不为空
                    for item in record_list:
                        write_file.write('\t\t' + item + '\n')
            else:
                write_file.write(line)
    #注意事项：只有当文件被关闭后，才可以执行以下两句；因为当有程序在使用文件时，无法执行删除等操作；
    #需要将当前文件删除后，才可以重命名；否则会报错(win10)
    os.remove('ha')
    os.rename('ha.new', 'ha')



if __name__ == '__main__':

    print('1、获取；2、添加；3、删除')
    num = input('请输入序号：')
    data = input('请输入内容：')
    if num == '1':
        if len(fetch(data)):
            print('\n'.join(fetch(data)))
        else:
            print("not find")
    else:
        dict_data = json.loads(data)
        if num == '2':
            add(dict_data)
        else:
            pass
            # data = "www.oldboy.org"
            # fetch(data)
            # data = '{"backend": "tettst.oldboy.org","record":{"server": "100.1.7.90","weight": 20,"maxconn": 30}}'
            # dict_data = json.loads(data)
            # add(dict_data)
            # remove(dict_data)
