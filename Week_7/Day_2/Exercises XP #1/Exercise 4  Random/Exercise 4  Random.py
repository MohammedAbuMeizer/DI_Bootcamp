import random

number = input("Enter a number in a range 1 to 100")
number = int(number)

def Accept(number):
    number_random = random.randint(0,100)
    if number >=1 and number <=100:
        if number ==number_random:
            print("sucses !!")
        else:
            print(f"fail : {number} not equal {number_random} ")
    else:
        print("Your number has to be in a range 1 to 100 .")


Accept(10)
Accept(number)