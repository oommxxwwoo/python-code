#列表

#定义/ 增 / 删 / 改 / 查 / 其他
#访问，切片，追加，插入，修改， 删除， 扩展， 拷贝， 统计， 排序，反转，获取下表

import copy
names = ["xiaoze", "wutenglan", "yuqian"]

print(names)

print(names[1])#访问
print(names[1:2])#切片，切片的方式为长生一个新的 列表
print(names[0:])




names.append("yueyunpeng")
names.insert(1, "yetianyou")
print(names)

#del names[1]
names.remove("wutenglan")
names[0] = "yangsiming"
#print(names.index("wutenglan"))

print(names)

for i in names:
    print(names.index(i),i)

names2 = ["a", "1menxiuwei"]
names.extend(names2)
print(names)

names.reverse()
print(names)
names.sort()
print(names)
print(names.count("a"))

names.append(["7899900","times"])
names3 = names.copy()
names4 = copy.deepcopy(names)
names.append("7899900")
names[6][0] = "libai"

print(names4)
print(names3)
print(names)

#元组，与列表的区别：元组只能读，不能修改，只有两种方法，index  count
ages = ("2", 'adkjs',"yushi")
age1 = (1,2,3,2,3,4,5,6)
print(ages,age1)
print(age1.index(1))
print(age1.count(2))