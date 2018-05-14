
import getpass

name = input("username:")
password = input("password:")
'''
password = getpass.getpass("password:")
'''

if name == "menxiuwei" and password == 'mxw6688':
    print("welcom {_name}to python".format(_name=name))
else:
    print("username or password erro! exit!")

print(name, password)