import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )#获取目录

print(sys.path)
sys.path.append(BASE_DIR)#设置环境变量...动态的设置环境变量


# from conf import settings
# from core import main
#
# main.login()