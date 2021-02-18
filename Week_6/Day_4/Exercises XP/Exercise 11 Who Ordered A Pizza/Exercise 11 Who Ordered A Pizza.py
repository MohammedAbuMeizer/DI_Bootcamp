series = input("Enter a topping or quit to exit : ")
list_topp = []
cal_result = 10

while series != "quit" :
    print("you’ll add that topping to their pizza")
    list_topp.append(series)
    series = input("Enter a topping or quit to exit : ")
    cal_result +=2.5

print(list_topp)
print(f"they have to pay  {cal_result}")