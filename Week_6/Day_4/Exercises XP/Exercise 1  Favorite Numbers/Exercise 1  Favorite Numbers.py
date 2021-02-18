my_fav_numbers  = {20,26,31}
print(my_fav_numbers)

my_fav_numbers.add(22)
print(my_fav_numbers)

my_fav_numbers.add(23)
print(my_fav_numbers)


my_fav_numbers.remove(31)
print(my_fav_numbers)

friend_fav_numbers = {30,31,25,22}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)