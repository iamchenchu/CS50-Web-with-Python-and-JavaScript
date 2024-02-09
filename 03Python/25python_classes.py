class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Chenchu", 27)

print(p1.name)
print(p1.age)
# print(p1) can't acees the object directly