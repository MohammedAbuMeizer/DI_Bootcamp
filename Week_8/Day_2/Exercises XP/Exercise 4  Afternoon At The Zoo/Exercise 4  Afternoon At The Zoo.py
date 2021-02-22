class Zoo:
    def __init__ (self , animals ,name ):
        self.animals = animals
        self.name = name
    
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for item in self.animals:
            print(item)
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self ):
        self.animals.sort()
        

zo = Zoo(["1","3","0"],"zoo")
zo.add_animal("lion")

zo.get_animals()

zo.sell_animal("lion")
zo.get_animals()

zo.sort_animals()

zo.get_animals()
