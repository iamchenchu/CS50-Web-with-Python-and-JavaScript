class Dog:
    attribute = "animal"

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("My name is {}".format(self.name))


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

#Accessing the class methods
Rodger.speak()
Tommy.speak()