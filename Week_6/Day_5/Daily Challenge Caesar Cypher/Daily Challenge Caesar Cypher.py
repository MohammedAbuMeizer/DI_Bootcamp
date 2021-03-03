enc_or_dec = input("if you want to encrypt type 1 , if you want to decrypt type 2 ")
shift = int(input("How much do you want to shift ? ")) 

def split(word):
    return [char for char in word] 
cypher_text = ""
 

if enc_or_dec == "1" :
    #enc
    text = input("Enter your text to encrypt : ")
    letter = split(text)
    for letter in text:
        cypher_text += chr(ord(letter) - shift)

elif enc_or_dec == "2" :
    #dec
    text = input("Enter your text to decrypt : ")
    letter = split(text)
    for letter in text:
        cypher_text += chr(ord(letter) + shift)
    

else :
    enc_or_dec = input("if you want to encrypt type 1 , if you want to decrypt type 2 ")
print(cypher_text)