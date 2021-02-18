option = input("Enter 1 to add name \nEnter 2 to remove a name from the list \nEnter 3 to view family members\nEnter 4 to exit")
listFamily = ["Ala"]
while option != "4" :
    if option == "1" :
        name = input("Enter a name to add : ")
        listFamily.append(name)
        option = input("Enter 1 to add name \nEnter 2 to remove a name from the list \nEnter 3 to view family members\nEnter 4 to exit")
    elif option == "2" :
        name = input("Enter a name to remove : ")
        if name in listFamily :
            listFamily.remove(name)
        else :
            print("there is no name like this")

        option = input("Enter 1 to add name \nEnter 2 to remove a name from the list \nEnter 3 to view family members\nEnter 4 to exit")

    elif option == "3" :
        print(listFamily)
        option = input("Enter 1 to add name \nEnter 2 to remove a name from the list \nEnter 3 to view family members\nEnter 4 to exit")
