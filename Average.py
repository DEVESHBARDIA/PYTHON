a = int(input("Enter marks-1"))
b = int(input("Enter marks-2"))
c = int(input("Enter marks-3"))
total = a+b+c
best_of_two = total - min(a,b,c)
average = best_of_two/2
print("Average is: ",average)
