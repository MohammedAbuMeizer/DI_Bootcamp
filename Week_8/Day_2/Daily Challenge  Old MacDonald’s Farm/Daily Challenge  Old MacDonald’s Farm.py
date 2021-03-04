
class Farm():
    def __init__(self,name):
        self.name = name
        self.animals = []
    def add_animal(self,animal_type, number = 1):
        new = (f"{animal_type} : {number}")
        if new not in self.animals:
            self.animals.append(new)
        elif new in self.animals and number !=1 :
            self.animals.remove(new)
            new = (f"{animal_type} : {number+number}")
            self.animals.append(new)
        elif new in self.animals and number ==1 :
            self.animals.remove(new)
            new = (f"{animal_type} : {number+number}")
            self.animals.append(new)
    def get_info(self):
        st = ""
        for item in self.animals:
            st = st + item + "\n"
        return(f"\n{self.name}'s farm\n\n{st} \n\n    E-I-E-I-0!\n")
    def get_animal_types(self):
        return sorted(self.animals)

    def get_short_info(self):
        result = ""
        list_n = self.get_animal_types()
        for item in range(len(list_n)-1):
            result = result + list_n[item] +","
        return (f"{self.name}’s farm has {result} and {list_n[len(list_n)-1]}.")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 12)


print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())


#print(animals)