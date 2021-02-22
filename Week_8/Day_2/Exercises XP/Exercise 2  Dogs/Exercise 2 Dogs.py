class Dogs:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def bark(self):
        print("goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height * 2 } cm high!")

davids_dog = Dogs("Rex", 50) 
sarahs_dog = Dogs("Teacup",20)  

davids_dog.jump()
davids_dog.bark()
sarahs_dog.jump()
sarahs_dog.bark()

if sarahs_dog.height > davids_dog.height:
    print(sarahs_dog.name) 
elif davids_dog.height > sarahs_dog.height:
    print(davids_dog.name) 
else :
    print("They are equally")