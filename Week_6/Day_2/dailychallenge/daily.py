import random
string = input('input a text min 10 letters\n')
if len(string) < 10:
    print('not long enough')
elif len(string) > 10:
    print('string is to long')
print(f'first letter: {string[0]} last letter: {string[-1]}')
new_string = ''
my_list = []
for i in range(0, len(string)):
    new_string += string[i]
    print(new_string)
    my_list.append(string[i])
random.shuffle(my_list)
new_word = ''
print(new_word.join(my_list))   