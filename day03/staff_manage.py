# -*- coding:utf-8 -*-
'''
用户列表示例
1,AlexLi,22,13651054608,IT,2013-04-01
2,熊荣琴,18,13800000000,IT,2017-12-13
3,李树彬,19,13812344321,TI,2011-10-12
4,赵华田,20,12856788765,IT,2009-10-23
5,王罗力,22,13889000987,IT,2010-10-22
6,陈俊民,24,13876543211,it,2011-11-11
使用前请创建一个 staff_table.txt 文件。
'''

import os

#字典，员工信息
staff_dict = {}

#表内信息的获取,保存在字典里面
def staff_read(str_file):
    list = []
    with open(str_file, 'r+', encoding='utf-8') as f:
        for i in f:
            if i.strip():#过滤掉空行
                list = i.strip().split(",")#将字符串转为列表
                staff_dict[list[1]] = list[2:]#添加字典元素
    return staff_dict



#{'熊荣琴': ['18', '13800000000', 'IT', '2017-12-13'], '王罗力': ['22', '13889000987', 'IT', '2010-10-22'], 'AlexLi': ['22', '13651054608', 'IT', '2013-04-01'], '李树彬': ['19', '13812344321', 'TI', '2011-10-12'], '赵华田': ['20', '12856788765', 'IT', '2009-10-23'], '陈俊民': ['24', '13876543211', 'ABC', '2011-11-11']}

def staff_write(str_file):
    with open(str_file, 'w+', encoding='utf-8') as f:
        line_num = 0
        for key in staff_dict:#遍历字典
            line = key + ' ' + ' '.join(staff_dict[key])#将字典的key，value转为字符串
            line = line.replace(" ", ",")#将字符串中的空格替换为逗号
            f.write( str(line_num) + ',' + line + '\n')#写入文件
            line_num += 1


staff_read("staff_excl")
staff_write("staff_new_excl")
os.remove("staff_excl")
os.rename("staff_new_excl", "staff_excl")



