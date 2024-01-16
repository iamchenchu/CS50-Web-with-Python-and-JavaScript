# Parent Class

class Person():

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My id number is {}".format(self.idnumber))


# Child Class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    def details(self):
        print("My name is {}, my Id number is {} working as {}, My salary is {} a month".format(self.name, self.idnumber, self.salary, self.post))

emp1 = Employee("Rahul", 11508605, "Manager", 200000)

emp1.display()
emp1.details()
