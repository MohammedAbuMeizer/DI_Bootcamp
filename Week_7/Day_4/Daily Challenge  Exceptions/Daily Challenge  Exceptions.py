import sys


number1 = input("Enter a first number : ")
number2 = input("Enter a second number : ")


def calculate_div(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    return number1/number2

try:
    print(calculate_div(number1,number2))
except:
     print("Error", sys.exc_info()[0], "occurred.")
else:
    print("Done without Errors")
finally:
  print("The 'try except' is finished")