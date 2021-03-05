from Dogs import Dog
import random

class PetDog(Dog):
    trained = False
    def __init__(self):
        self.trained = False
    
    def train(self,*dogs):
        for dog in dogs :
            dog.bark() 
            dog.trained = True
    
    def play(self,*dogs):
        result = ""
        for dog in dogs:
            dog.trained = False
            result = result +  dog.name + ", " 
        return "The dogs: " +result + "play together"

    def do_a_trick(self,*dogs):
        for dog in dogs:
            if dog.trained == True:
                dog.trained = False
                trai = [' does a barrel roll'
                , ' stands on their back legs'
                , ' shakes your hand'
                , ' plays dead']
                print(f"{dog.name}" + random.choice(trai))
            else:
                print(f"{dog.name} trained is {dog.trained}")
        return("\n(((do_a_trick methode done)))\n")

wiskey = Dog("wiskey",15,20)
hiskey = Dog("hiskey",5,15)
niskey = Dog("niskey",15,20)

petDog = PetDog()

print(petDog.play(wiskey,hiskey,niskey))
#print(wiskey.trained)
petDog.train(wiskey,hiskey)
print(wiskey.trained)
print(hiskey.trained)
print(niskey.trained)
print(petDog.do_a_trick(wiskey,hiskey,niskey))
print(petDog.do_a_trick(wiskey,hiskey))
#print(petDog.do_a_trick(niskey))

