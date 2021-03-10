class Currency():

    def __init__(self,currency,value):
        self.currency = currency
        self.value = value
    
    def __str__(self):
       # print(f"'{self.value} {self.currency}s'")
        return f"'{self.value} {self.currency}s'"
    
    def __int__(self):
        return self.value
    def __repr__(self):
        #print(f"'{self.value} {self.currency}s'")
        return f"'{self.value} {self.currency}s'"

   
    
    def __add__(self,other):
        if other in range(0,1000) :
            return self.value + other
        elif self.currency == other.currency:
            return self.value + other.value
        else :
            return(f"TypeError: Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self,other):
        if other in range(0,1000) :
            self.value = self.value + other
            return self.value
        elif self.currency == other.currency:
            self.value = self.value + other.value
            return self.value
        else :
            return(f"TypeError: Cannot add between Currency type <{self.currency}> and <{other.currency}>")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1 + c3)
print(c1)
c1 += c3
print(c1)
