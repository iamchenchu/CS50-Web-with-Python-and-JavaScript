"""__dict__	It provides the dictionary containing the information about the class namespace.
__doc__	It contains a string which has the class documentation
__name__	It is used to access the class name.
__module__	It is used to access the module in which, this class is defined.
__bases__	It contains a tuple including all base classes."""

class Student :
    def __init__(self, name, id, age):
        self.name = name
        self.id = id 
        self.age = age 
    def display_details(self):
        # print("Name :%s, ID:%d, age:%d"%(self.name, self.id))
        print("Name :{},\n Id : {}, \n Age :{}".format(self.name, self.id, self.age))
    
s = Student("Chenchu", 115086, 26)

#print(s.__doc__)
#print(s.__dict__)
#print(s.__module__)
print(s.display_details())