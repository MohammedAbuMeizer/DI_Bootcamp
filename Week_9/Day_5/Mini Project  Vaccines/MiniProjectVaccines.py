class Human():
    def __init__(self,id_number,name,age,prioritary,blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.prioritary = prioritary
        self.blood_type = blood_type

class Queue():
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        for item in self.queue:
            print(item.name)

    def size(self):
        return len(self.queue)
    
    def add_person(self, person):
        l = []
        if len(self.queue) < 1:
            self.enqueue(person)
        elif person.age > 60 or (person.prioritary == True):
            l = self.queue
            self.queue = []
            self.enqueue(person)
            for item in l :
                self.enqueue(item)
        else:
            self.enqueue(person)
    def find_in_queue(self, person):
        index = 0
        for item in self.queue :
            index += 1
            if item.id_number == person.id_number :
                return(index-1)
                
    def swap(self, person1, person2):
        p1_index = int(self.find_in_queue(person1))
        p2_index = int(self.find_in_queue(person2))
        temp = ""
        temp = self.queue[p1_index]
        self.queue[p1_index] = self.queue[p2_index]
        self.queue[p2_index] = temp

    def get_next(self):
        self.dequeue()
    
    def get_next_blood_type(self, blood_type):
        for item in self.queue:
            if item.blood_type == blood_type:
                return self.dequeue()

    def sort_by_age(self):
        for ind in range(0,len(self.queue)-1):
            if self.queue[ind].age < self.queue[ind+1].age: 
                if self.queue[ind].prioritary == True and self.queue[ind+1].prioritary == False :
                    self.swap(self.queue[ind],self.queue[ind+1])
                    print("@@@@@")
        #return self.queue
           
        

h1 = Human("1","h1",60,False,"A")
h2 = Human("2","h2",61,True,"B")
h3 = Human("3","h3",14,False,"AB")
h4 = Human("4","h4",70,False,"O")
h5 = Human("5","h5",22,True,"A")
q = Queue()
q.add_person(h1)
q.add_person(h2)
q.add_person(h3)
q.add_person(h4)
q.add_person(h5)
q.display()
print("########")
q.sort_by_age()
q.display()
print("########")
q.find_in_queue(h1)
q.find_in_queue(h2)
q.find_in_queue(h3)
q.find_in_queue(h4)
q.find_in_queue(h5)
q.get_next()

q.display()