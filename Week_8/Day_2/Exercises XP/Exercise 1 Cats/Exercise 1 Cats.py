class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def the_oldest(self,another_cat1,another_cat2):
        if self.age > another_cat1.age and self.age > another_cat2.age:
            return self
        elif  another_cat1.age > self.age and another_cat1.age >another_cat2.age:
            return  another_cat1
        elif  another_cat2.age > self.age and another_cat2.age >another_cat1.age:
            return  another_cat2

cat_1 = Cat("cat 1",5)
cat_2 = Cat("cat 2",6)
cat_3 = Cat("cat 3",7)

print(f"The oldest cat is {Cat.the_oldest(cat_1,cat_2,cat_3).name} , and {Cat.the_oldest(cat_1,cat_2,cat_3).age} is years old")
