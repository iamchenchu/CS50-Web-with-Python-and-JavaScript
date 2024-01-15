n = int(input("Number : "))  # By default the number will be consider as a string
# So we have to explicitly define the type of the input as int
if n > 0:
    print(f"{n}, is positive")
elif n == 0 :
    print(f"{n}, is zero")
else:
    print(f"{n}, is Negative")