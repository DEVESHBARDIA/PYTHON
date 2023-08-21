class palindrome_string:
    def __init__(self):
        self.p = False

    def check(self, str1):
        if str1 == str1[::-1]:
            self.p = True
        else:
            self.p = False
        return self.p


class plaindrome_int(palindrome_string):
    def __init__(self):
        self.p = False

    def check(self, n):
        temp = n
        rev = 0
        while n != 0:
            rem = n % 10
            rev = (rev * 10) + rem
            n = n // 10

        if temp == rev:
            self.p = True
        else:
            self.p = False
        return self.p


s = input("Enter a string: ")
obj1 = palindrome_string()
if obj1.check(s):
    print("String is Palindrome")
else:
    print("String is not Palindrome")

i = int(input("Enter a number:"))
obj2 = plaindrome_int()
if obj2.check(i):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
