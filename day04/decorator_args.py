# -*- coding:utf-8 -*-


'''
装饰器自身加参数
被装饰的函数有参数和返回值

'''

def auth(auth_type):
    print(auth_type)
    def out_wapper(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res#被修饰函数的返回值在此处返回
        return wrapper
    return out_wapper




def index():
    print("welcome to index page")
@auth(auth_type = "local")
def home():
    print("welcome to home  page")
    return "from home"

@auth(auth_type = "ldap")
def bbs():
    print("welcome to bbs  page")

index()
print(home()) #wrapper()
bbs()