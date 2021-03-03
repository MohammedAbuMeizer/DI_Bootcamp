users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

disney_users_A = {}
disney_users_B = {}
disney_users_C = {}

ind = 0 
for item in users :
    disney_users_A[item] = ind
    ind += 1
print(disney_users_A)

ind = 0 

for item in users :
    disney_users_B[ind] = item
    ind += 1
print(disney_users_B)

ind = 0

for item in sorted(users) :
    disney_users_C[item] = ind
    ind += 1
print(disney_users_C)

ind = 0 

def split(word):
    return [char for char in word] 

disney_users_A = {}
for item in users :
    if "i" in item :
        sp = split(item) 
        if "M" == sp[0] or "P" == sp[0]:
            disney_users_A[item] = ind
            ind += 1
print(disney_users_A)
