matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]
string_to_print = ''
for i in range(len(matrix[4])):
	for n in range(len(matrix)):
		letter = matrix[n][i]
		if letter.isalpha():
			string_to_print += letter
		else:
			try:
				if string_to_print[-1] != ' ':
					string_to_print += ' '
			except:
				print('our string is empty, lets move to next iteration')
print(string_to_print)
