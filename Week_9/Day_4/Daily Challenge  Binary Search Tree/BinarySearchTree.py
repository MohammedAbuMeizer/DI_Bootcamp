class Node():

    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
    
    def set_left(self ,node):
        self.left = node

    def set_right(self ,node):
        self.right = node
    
    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value
    
    
 
    def add_node(self,node):
        if node.get_value() == self.get_value():
            return #its equal

        if node.get_value() <  self.get_value():
            self.set_left(node)
            if self.get_left():
                self.get_left().add_node(node)
            else:
                self.left = Node(node)
                return self.left
        elif node.get_value() > self.get_value():
            self.set_right(node)
            if self.get_right():
                self.get_right().add_node(node)
            else:
                self.right = Node(node)
                return self.right
                
    def search(self,value):
        if self.get_value() == value:
            return f"we have a node = {Node(value).value}"
            
        if value < self.get_value():
            if self.get_left():
                return self.get_left().search(value)
            else:
                return f"there is no node = {value}"
        if value > self.get_value():
            if self.get_right():
                return self.get_right().search(value)
            else:
                return f"there is no node = {value}"
        

n1 = Node(5)
n2 = Node(6)
n3 = Node(5)
n4 = Node(4)

n1.add_node(n2)
n1.add_node(n3)
n1.add_node(n4)
print(n1.search(3))
print(n1.search(5))
print(n1.search(4))
print(n1.search(2))
print(n1.search(7))






