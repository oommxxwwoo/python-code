
print("this is a person manager system \r\n")

#input类型默认为字符串类型
name = input("name:")
print(type(name))
age = int(input("age:"))#强制转换为int类型,怎么判断age为数字，而不是字符呢？
if age >= 0 and age <=100:
    print("age = ", age)
    age = int(age)
else:
    print("please input right age ,is must be digital")
job = input("job:")
salary = (int)(input("salary:"))


info =''' --------info %s----------
name:%s
age:%d
job:%s
salary:%d
'''%(name,name,age,job,salary)


info1 = ''' -------info {_name}--------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,
           _job=job,
           _age=age,
           _salary=salary,
           )

print(info1)


