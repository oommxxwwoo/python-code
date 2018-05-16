
product_list = [
    ("iphone", 6000),
    ("coffe", 32),
    ("book linux", 61),
    ("bickle", 600)
]

shopping_list = []

print(product_list)

salary = input("you salary:")
if salary.isdigit():#是否为数字
    salary = int(salary)
    #print(salary)
    while True:
        for item in product_list:#打印商品列表
            print(product_list.index(item),item)
        choise = input("choice numbe to put in shoping car:")
        if choise.isdigit():
            choise = int(choise)
            if choise >= 0 and choise < len(product_list):
                if salary > product_list[choise][1]:
                    salary = salary - product_list[choise][1]
                    shopping_list.append(product_list[choise])#追加到购物车列表
                    print("you balance = ",salary)
                else:
                    print("you balance is not to pay")

            else:
                print("choice number erro , balance = ",salary)
        else:
            if(choise == 'b'):
                print('==============================')
                for item in shopping_list:
                    print(item)
                print("you balance =", salary)
                break;

else:
    print("input erro")