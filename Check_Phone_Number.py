import re


def checkphonenumber1(numStr):
    if len(numStr) != 12:
        return False
    for i in range(len(numStr)):
        if i == 3 or i == 7:
            if numStr[i] != "-":
                return False
        else:
            if not numStr[i].isdigit():  # alternate: numStr[i].isdigit() == False:
                return False
    return True


def checkphonenumber2(numstr):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(numstr):
        return True
    else:
        return False


ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if checkphonenumber1(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression")
if checkphonenumber2(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

