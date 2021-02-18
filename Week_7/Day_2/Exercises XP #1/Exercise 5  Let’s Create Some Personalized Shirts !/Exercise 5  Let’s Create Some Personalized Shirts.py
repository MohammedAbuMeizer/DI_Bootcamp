

def make_shirt(*shirt,sentence):
    index= 0
    for item in shirt:
        print(f"{shirt[index]}  {sentence} ")
        index = index + 1

make_shirt("L","M","S",sentence = "i")

def make_shirt(*args,sentence):
    sentence = "i love python"
    index= 0
    for item in args:
        print(f"{args[index]}  {sentence} ")
        index = index + 1

make_shirt("L","M","S",sentence="")



