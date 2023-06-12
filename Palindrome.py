num = int(input("Enter the number: "))
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp%10
    temp = temp//10
print(rev == num)
count = {}
num = str(num)
for i in num:
    count[i] = num.count(i)
print(count)
