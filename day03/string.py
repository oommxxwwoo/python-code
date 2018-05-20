__author__ = "Alex Li"


name = "my \tname is {name} and i am {year} old"

print(name.capitalize())#首字母大写
print(name.count("a"))#a出现的个数
print(name.center(50,"-"))#居中对齐，不足50字符补-
print(name.endswith("ex"))#以某某结束
print(name.expandtabs(tabsize=30))#tab 制表符代码几个字符长度
print(name[name.find("name"):])#查找字符出现的位置
print(name.format(name='alex',year=23))#formet格式
print(name.format_map(  {'name':'alex','year':12}  ))
print('ab23'.isalnum())#是否为阿拉伯数字
print('abA'.isalpha())#
print('1A'.isdecimal())#是否为十进制字符
print('1A'.isdigit())#是否为数字
print('a 1A'.isidentifier()) #判读是不是一个合法的标识符
print('33A'.isnumeric())
print('My Name Is  '.istitle())#是否为标题
print('My Name Is  '.isprintable()) #是否可打印 tty file ,drive file
print('My Name Is  '.isupper())#是否第一个为大写
print('+'.join( ['1','2','3'])  )#列表转换为字符串
print( name.ljust(50,'*')  )#左边调整50间距
print( name.rjust(50,'-')  )
print( 'Alex'.lower()  )#小写
print( 'Alex'.upper()  )#大写
print( '\nAlex'.lstrip()  )#左边
print( 'Alex\n'.rstrip()  )
print( '    Alex\n'.strip()  )#过滤掉空格和换行符

#以下两行可用作  密码
p = str.maketrans("abcdefli",'123$@456')#设置转换关系
print("alex li".translate(p) )#使用 转换关系p，进行字符转码

print('alex li'.replace('l','L',1))#替换
print('alex lil'.rfind('l'))#从左边找，返回位置
print('1+2+3+4'.split('\n'))#去除换行
print('1+2\n+3+4'.splitlines())
print('Alex Li'.swapcase())#大小写反转
print('lex li'.title())#成为标题
print('lex li'.zfill(50))#补0凑够50字符

print( '---')

