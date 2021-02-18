fav = input("Enter your favorite fruits devided by space : ")
result = ""
list_fav_fruits = fav.split(" ")

any_fruit = input("Enter any friut name : ")

if any_fruit in list_fav_fruits :
    print("You chose one of your favorite fruits! Enjoy!")
else :
    print("You chose a new fruit. I hope you enjoy it too!")

item = 0

for friut in list_fav_fruits :
    if item == len(list_fav_fruits) - 1 and len(list_fav_fruits) > 1:
        result = result + " and " + friut
    else :
         result = result  + friut+ " | "
         item+=1

print(result)
