import datetime

your_date = input("Enter your age in this format (DD/MM/YYYY) : ")

our_date = datetime.datetime.now()

year = your_date.split("/")

your_age = our_date.year - int(year[2])

candles_num = your_age % 10 

crown = ""

print(candles_num)


candles = ["_","_","_","_","_","_","_","_","_","_","_"]

if candles_num == 1 :
    candles[5]= "i"
elif candles_num == 2 :
    candles[5]= "i"
    candles[4]= "i"
elif candles_num == 3 :
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
elif candles_num == 4 :
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
    candles[3]= "i"
elif candles_num == 5 :
    candles[7]= "i"
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
    candles[3]= "i"
elif candles_num == 6 :
    candles[7]= "i"
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
    candles[3]= "i"
    candles[2]= "i"
elif candles_num == 7 :
    candles[8]= "i"
    candles[7]= "i"
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
    candles[3]= "i"
    candles[2]= "i"
elif candles_num == 8 :
    candles[8]= "i"
    candles[7]= "i"
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
    candles[3]= "i"
    candles[2]= "i"
    candles[1]= "i"
elif candles_num == 9 :
    candles[9]= "i"
    candles[8]= "i"
    candles[7]= "i"
    candles[6]= "i"
    candles[5]= "i"
    candles[4]= "i"
    candles[3]= "i"
    candles[2]= "i"
    candles[1]= "i"

for candle in candles :
    crown = crown + candle 

print(f"       {crown}")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~\n")
