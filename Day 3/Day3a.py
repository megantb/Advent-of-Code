from itertools import islice

file1 = open("Day3Input.txt", 'r')
lines = file1.readlines()


sum1 = 0

for line in lines:
  string = line
  x, y = string[:len(string)//2], string[len(string)//2:]
  a=list(set(x)&set(y))
  for i in a:
    num = ord(i)-96
    if i.islower():
        num = ord(i)-96
    elif i.isupper():
        num = ord(i.lower())-96+26

    sum1 = sum1 + num


print(sum1)