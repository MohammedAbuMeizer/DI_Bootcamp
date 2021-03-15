import string 
import random 
length = 5
result = ''.join(random.choices(string.ascii_letters, k = length)) 
  
print("The generated random string : " + str(result)) 