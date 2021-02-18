list_of_magicians = ["name1","name2","name3","name4"]

def show_magicians(list_of_magicians):
    for item in list_of_magicians:
        print(item)

show_magicians(list_of_magicians)

def make_great(list_of_magicians):
    index = 0
    for item in list_of_magicians:
        list_of_magicians[index] = list_of_magicians[index] + " the graet"
        index = index+1

make_great(list_of_magicians)
show_magicians(list_of_magicians)