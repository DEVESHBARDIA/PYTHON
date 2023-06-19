sentence = input("Enter a sentence: ")
w, d, u, l, s = 0, 0, 0, 0, 0
sen = sentence.split()
w = len(sen)
for c in sentence:
    if c.isdigit():
        d = d + 1
    elif c.isupper():
        u = u + 1
    elif c.islower():
        l = l + 1
    elif c.isspace():
        s = s + 1

print("No of Words: ", w)
print("No of Digits: ", d)
print("No of Uppercase letters: ", u)
print("No of Lowercase letters: ", l)
print("No of Spaces:", s)


