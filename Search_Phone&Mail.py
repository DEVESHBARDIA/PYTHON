import re


phone = re.compile(r'\+\d{12}')
email = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z][A-Za-z][A-Za-z]')
with open('phone.txt', 'r') as f:
    for x in f:
        matches = phone.findall(x)
        for i in matches:
            print(i)

        matches = email.findall(x)
        for y in matches:
            print(y)
