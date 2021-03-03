ages = []
names =[]
inputes1 = input("Enter name for each one in family separated by comma :")
inputes2 = input("Enter age for each one in family separated by comma :")

names = inputes1.split(",")
ages = inputes2.split(",")

family = zip(names,ages)
family=dict(family)
print(f"your family with ages : {family}")
total = 0

for age in family.values():
    age = int(age)
    if age < 3 :
        total = total + 0 
        age = int(age)

    elif age >= 3 and age <= 12 :
        total = total + 10 
        age = int(age)
    elif age > 12 :
        total = total + 15
        age = int(age)


print(f"family’s total cost for the movies : {total}$")






# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total = 0

# for age in family.values():
#     if age < 3 :
#         total = total + 0 
#         age = int(age)

#     elif age >= 3 and age <= 12 :
#         total = total + 10 
#         age = int(age)
#     elif age > 12 :
#         total = total + 15
#         age = int(age)


# print(f"family’s total cost for the movies : {total}$")

