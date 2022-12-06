from collections import Counter

with open('Year2022/Day6/Day6Input.txt') as f:
  data = f.read().strip()

for n in (4, 14):
  for i in range(len(data)):
    s = data[i : i + n]
    if len(set(s)) == len(s):
      print(i + n)
      break
        
              
  