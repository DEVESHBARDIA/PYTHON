def fn(n):
    if n<=1:
        return n
    else:
        return fn(n - 1)+fn(n - 2)


n = int(input("Enter the number: "))
if n<0:
    print("Number should be more than 0")
else:
    for x in range(0,n):
        print(fn(x), end=" ")
