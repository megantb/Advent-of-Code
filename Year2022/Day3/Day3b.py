from itertools import islice
import linecache
sum2=0
with open('Day3/Day3Input.txt') as file:
  while True:
    next_n_lines = list(islice(file, 3))
    if not next_n_lines:
      break
    #assign lines to variables
    #print(next_n_lines[0])
    x = next_n_lines[0]
    y = next_n_lines[1]
    z = next_n_lines[2]

    a=list(set(x)&set(y)&set(z))
    for i in a:
      if i.islower():
        num = ord(i)-96
      elif i.isupper():
        num = ord(i.lower())-96+26

    sum2 = sum2 + num


print(sum2)
  

