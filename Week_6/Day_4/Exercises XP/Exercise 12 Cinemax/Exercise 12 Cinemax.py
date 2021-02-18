age = input("enter your age please or exit: ")
age = int(age)

total = 0

while age != -1 :
    if age < 3 :
        total = total + 0 
        age = input("enter your age please or exit: ")
        age = int(age)

    elif age >= 3 and age <= 12 :
        total = total + 10 
        age = input("enter your age please or exit: ")
        age = int(age)


    elif age > 12 :
        total = total + 15
        age = input("enter your age please or exit: ")
        age = int(age)


print(total)


age = input("enter your age please or -1: ")
age = int(age)
teen = []

while age != -1 :
    if age >=16 and age<=21 :
        print("you can see the movie")
        age = input("enter your age please or -1: ")
        age = int(age)
        teen .append(age)
    else :
        print("you cant see the movie")
        age = input("enter your age please or -1: ")
        age = int(age)

print(teen)