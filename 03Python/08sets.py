#Create an empty set
s = set()


#Add the elements to the set, won't save again for repeated values
s.add(3)
s.add(3)
s.add(4)
s.add(2)
s.add(1)


print(s)
s.remove(3) # Removes both indexes which contains the value 3
print(s) 

print(f"The set has {len(s)} elements")