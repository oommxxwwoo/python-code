
#商品列表
shoppingGoods = [('Macbook Air', 7999), ('Starbucks Coffee', 33), ('Iphone 6 plus', 5188)]
#购物车列表
shoppingList = {}

def show_goods():
    for index, item in enumerate(shoppingGoods):
        print(index, shoppingGoods[index])

show_goods()
0 ('Macbook Air', 7999)
1 ('Starbucks Coffee', 33)
2 ('Iphone 6 plus', 5188)
'''

show_shoppingList()