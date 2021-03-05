class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    def walk(self):
         return f'{self.name} is just walking bengal' 

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Breed(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal = Bengal("bengal",4)
chartreux = Chartreux("chartreux",5)
breed = Breed("breed",6)

my_cats = []
my_cats.append(bengal)
my_cats.append(chartreux)
my_cats.append(breed)

my_pets = Pets(my_cats)
my_pets.walk()

