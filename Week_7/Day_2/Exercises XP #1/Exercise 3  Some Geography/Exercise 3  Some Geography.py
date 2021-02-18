cities_in_America = ("florida","texas") 
name_of_city = input("Enter city : ")

def describe_city(name_of_city,country = "America"):
    if name_of_city in cities_in_America:
        print(f"{name_of_city} is in {country} ")
    else :
        print(f"{name_of_city} is not in {country} ")


describe_city(name_of_city,country="America")
describe_city(name_of_city="florida",country="America")
describe_city(name_of_city="texas",country="America")
describe_city(name_of_city="noco",country="America")