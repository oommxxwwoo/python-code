

shandong = {
    "菏泽":{"巨野":["龙固", "太平", "田桥","谢集"],
            "定陶县":["斋集","大鹏"]

          },
    "济南":{"历城区":["鲍山", "济钢", "王舍人"],
            "历下区":["软件园","奥盛大厦","新盛大厦"]

          }


}

print(shandong)

# 三级菜单

while True:
    for key in shandong:
        print(key)
    choice = input("please input you want in:")
    if choice in shandong:
        while True:
            for key1 in shandong[choice]:
                print(key1)
            choice1 = input("you want to in:")
            if choice1 in shandong[choice]:
                while True:
                    for key2 in shandong[choice][choice1]:
                        print(key2)
                    if 'b' == input("选择:"):
                        break;
            else:
                if choice1 == 'b':
                    break;

    else:
        if choice == 'b':
            break;

