from itertools import islice

inc_count=1

with open('Year2021/Day1/Day1Input.txt') as f:
  linex = next(f)  #get first line
  for line in f:
    if linex.rstrip() < line.rstrip():
      inc_count = inc_count +1
    linex = line
  
print(inc_count)
 
    