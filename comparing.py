# Compare two strings using == operator
a = input("String-1")
b = input("String-2")

if a == b:
    print("Similar")
else:
    print("not similar")

# Compare two strings using relational operator
b = input("String-2")
a = input("String-1")
if a > b:
    print(a, "is grater than", b)
elif a < b:
    print(b, "is grater than", a)

#Compare two strings using 'is' operator - id of the object should be same
a = input("String-1")
b = input("String-2")
c = a
print(a is b)
print(b is a)
print(a is c)

#Compare two strings ignoring white spaces - removes white space from the begnning

a = input("String-1")
b = input("String-2")
print(a.strip() == b.strip())

