import math
class Circle():

    def __init__(self,radius):
        self.radius = radius
        self.__diameter = self.radius * 2
        self.__area = math.pi * math.pow(self.radius,2)
    
    @property
    def diameter(self):
        self.__diameter = self.radius *2
        return  self.__diameter

    @diameter.setter
    def diameter(self,value):
        self.__diameter = value
        self.radius = int(value / 2 )
        
    @property
    def area(self):
        self.__area = math.pi * math.pow(self.radius,2)
        return  self.__area

    @classmethod
    def from_diameter(cls,value):
        Circle.radius = int(value / 2 )
        Circle.diameter = value
        radius = Circle.radius
        return  cls(radius)
    
    def __str__(self):
        return "Circle with radius : %0.6f"%self.radius

    def __repr__(self):
        #print(f"'Circle({self.radius})'")
        return f"'Circle({self.radius})'"

    def __add__(self,other):
        return f"Class({self.radius + other.radius})"

    def __mul__(self,value):
        return f"Class({self.radius * value})"
    
    def __gt__(self,other):
        if self.radius > other.radius:
            return True
        return False
    def __lt__(self,other):
        if self.radius < other.radius:
            return True
        return False
    
    def __eq__(self,other):
        if self.radius == other.radius:
            return True
        return False




c = Circle(2)
print(c.radius)
print(c.diameter)
print(c.area)
c.diameter = 2 
print(c.diameter)
print(c.radius)
print(c.area)
c.radius = 3 
print(c.diameter)
print(c.area)
c = Circle.from_diameter(2)
print("____")
print(c.diameter)
print(c.radius)
print(c.area)
print(c)
repr(c)
c1 = Circle(2)
c2 = Circle(4)
print(c1 + c2)
print(c1 * 3)
print(c1 > c2 )
print(c1 < c2 )
print(c2 < c1 )

print(c1 == c2)
circles = []

circles.append(c1)
circles.append(c2)
circles.append(c)

print(circles)
circles.sort()
print(circles)
