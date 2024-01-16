"""getattr(obj,name,default)	It is used to access the attribute of the object.
setattr(obj, name,value)	It is used to set a particular value to the specific attribute of an object.
delattr(obj, name)	It is used to delete a specific attribute.
hasattr(obj, name)	It returns true if the object contains some specific attribute."""

class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id 
        self.age = age 

# Create the object of the class Student 
s = Student("Chenchu", 11508605, 28)

# prints the attribute name pf the object s
print(getattr(s,'name'))

# reset the value of attribute age 23
setattr(s, "age", 26)

# Prints the modified attribute
print(getattr(s, 'age'))

#Prints true if the student contains the attribute with name id

print(hasattr(s, 'id'))
#deletes the attribute age
delattr(s, 'age')

#this will give an erroe since the attribute age has been deleted
print(s.age)

