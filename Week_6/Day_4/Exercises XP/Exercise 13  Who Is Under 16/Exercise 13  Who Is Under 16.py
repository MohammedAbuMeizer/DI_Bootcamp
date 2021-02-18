list_of_users = ["jhon","mike","sally"]
name = input("Enter your name : ")
age = input("Enter your age : ")
age = int(age)

if name in list_of_users :
    if age < 16 :
        list_of_users.remove(name)
else :
    print("your name is not in our list")


print(list_of_users)