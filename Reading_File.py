import os.path
import sys

filename = input("Enter the filename : ")
n = int(input("Enter the number of lines u want to read: "))
word = input("Enter a word : ")
count = 0
f = open(filename, "r")
lines = f.readlines()
for i in range(n):
    print(i + 1, ":", lines[i].replace('\n', ''))
for line in lines:
    count += line.count(word)
print("The word", word, "appears", count, "times in the file")


# filename = input("Enter filename: ")
# n = 10
# word = 'the'
# f = open(filename)
# content = f.read()
# lines = content.split("\n")
# print(lines[0:n])
# print(content.count(word))
# f.close()
