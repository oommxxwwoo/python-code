
#商品列表
shoppingGoods = [('Macbook Air', 7999), ('Starbucks Coffee', 33), ('Iphone 6 plus', 5188)]
#购物车列表
shoppingList = {}

def show_goods():
    for index, item in enumerate(shoppingGoods):#enumerate为枚举的意思，参数为object ，返回（0， swq(0)）,(1, seq(1)).....
        print(index, shoppingGoods[index])
    print('q buy and quit'.center(4,'*'))

def show_shoppingList():
    comsume = 0
    for key in shoppingList:
        comsume += key[1] * shoppingList[key]#计算总金额
    for index,item in enumerate(shoppingList):
        #print(index, item, shoppingList[item])
        print("NO: %s %s count %s".center(20,'-') %(index, item, shoppingList[item]))
    print('your total comsume is %d yuan'.center(20,'-') %comsume)
    print('your left money is %d yuan'.center(20,'-') %totalMoney)

while True:
    money = input("Enter your Money:")
    if not money.isdigit():
        print("input err")
    else:
        break
totalMoney = int(money)
print("Welcome to the JD shop!")

while True:
    show_goods()
    no = input('which one do you want?:')
    if  no == 'q':
        show_shoppingList()
        break
    if not no.isdigit():
        continue
    no = int(no)
    print(no)
    if no >= 0 and no < len(shoppingGoods):
        if totalMoney < shoppingGoods[no][1]:
            print('sorry, your balance is insufficient')
        else:
            totalMoney -= shoppingGoods[no][1]
            if shoppingList.get(shoppingGoods[no]):
                shoppingList[(shoppingGoods[no])] = shoppingList.get(shoppingGoods[no]) + 1
            else:
                shoppingList[(shoppingGoods[no])] = 1
            print('you buy a %s'.center(20,'-') %shoppingGoods[no][0])
            #打印当前购物车
            for index,item in enumerate(shoppingList):
                print("NO: %s %s count %s".center(20,'-') %(index, item, shoppingList[item]))
    else:
        show_shoppingList()

print('Bye bye')