from random import randint

def fun(num):
    if num in range(0,100):
        rand_num = randint(0,100)
        print(rand_num)
        if num == rand_num:
            print("Success")
    return print("num between 1 and 100 ")

fun(10)