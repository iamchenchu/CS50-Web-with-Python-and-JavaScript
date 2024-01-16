class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

class Dog:
    # Class attribute
    attribute1 = "mammal"

    #Instance attributes
    def __init__(self, name):
        self.name = name
    
#Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

#Accessing the class attrubutes
print("Rodger is a {}".format(Rodger.__class__.attribute1))
print("Tommy is also a {}".format(Tommy.__class__.attribute1))

#Accessing the instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


