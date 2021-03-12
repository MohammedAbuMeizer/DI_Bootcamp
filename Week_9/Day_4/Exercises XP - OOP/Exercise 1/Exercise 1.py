class Human():

    def __init__(self,name,age,living_place):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building.address
        building.inhabitants.append(self)

class Building():

    def __init__(self,address = "None",inhabitants = []):
        self.address = address
        self.inhabitants = inhabitants

    

class City():
    buildings = []
    def __init__(self,name,buildings):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        bul = Building(address)
        self.buildings.append(bul) 

    def info(self, address):
        num_of_B = 0
        num_of_H = 0
        build = ""
        mean = 0 
        for bulding in self.buildings:
            if bulding.address == address:
                build = address
                for human in bulding.inhabitants:
                    if human.living_place == address:
                        num_of_H += 1
                        num_of_B += 1
                        mean = mean + human.age
                return f"number buildings are {num_of_B} in {build}\nmean age is {mean/num_of_H}"
        return f"there is no  buildings in {address}"
h1 = Human("mohamed",26,"jerusalem")
h2 = Human("rda",22,"moroco")
h3 = Human("alla",23,"moroco")
h4 = Human("mohamed",25,"jerusalem")

hum_ar = []
hum1_ar = []
build = []
hum_ar.append(h1)
hum_ar.append(h4)
hum1_ar.append(h2)
hum1_ar.append(h3)
print(h1.living_place)
print(h1.name)
b1 = Building("jerusalem",hum_ar)
b2 = Building("moroco",hum1_ar)
b3 = Building("Ramallah")
build.append(b1)
build.append(b2)
c = City("israel",build)
h1.move(b3)
print(h1.living_place)
print(h1.name)
c.construct("Ramallah")
print(c.info("jerusalem"))
print(c.info("moroco"))
print(c.info("Ramallah"))

print(c.info("no"))





