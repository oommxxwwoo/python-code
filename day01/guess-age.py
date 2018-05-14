

print("this a game ", "guess age" )

my_age = 28

conut = 0
while conut < 3:
    age = int(input("please guess my age:"))
    if age > my_age:
        print("guess smaler..")
    elif age < my_age:
        print("guess bigger")
    else:
        print("right! ,age =", age)
        break
    conut += 1
    if(conut >= 3):
       continue_firm = input("is guess 3 times, are you continues..?")
       if continue_firm != 'n':
            conut = 0
#else:
    #print("it guess more times ,eixt!")