import random,string

my_file = open("sowpods.txt","r")


def get_words_from_file():
    list_contents = []
    for _ in my_file:
        list_contents.append(my_file.readline().strip()+" ")
    return list_contents


def get_random_sentence(length):
    result = ''.join(random.choices(get_words_from_file(), k = length)) 
    print("The generated random sentence : " + str.lower((result)))
    

 

def main():
    print("Random Sentence Generator")
    length = int(input("Enter 2-20 words to get randomly in sentence :"))
    if 1 < length < 21 :
        get_random_sentence(length)
    else:
        print("Incorrect data")

main()