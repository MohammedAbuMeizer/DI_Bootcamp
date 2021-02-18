
def check(num):
    degit = 0

    while num > 0 :
        rem = num % 10
        degit += rem
        num = int(num / 10)
    return ((degit % 7) == 0)

min_number = 1500
max_number = 2701
list_numbers = []

for num in range(min_number,max_number) :
    if (num % 5) == 0 :
        if check(num) :
            list_numbers.append(num)


print(list_numbers)