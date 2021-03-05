class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight =weight
    
    def bark(self):
        return "barks"
    
    def run_speed(self):
        if self.age <= 0 :
            return "You cant be 0 or less"
        return (self.weight / (self.age *10))
    
    def fight(self,other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight :
            return f"{self.name} should win"
        elif self.run_speed() * self.weight == other_dog.run_speed() * other_dog.weight :
            return "we cant know"
        return f"{other_dog.name} should win"

wiskey = Dog("wikey",15,20)
hiskey = Dog("hikey",5,15)
niskey = Dog("nikey",15,20)
