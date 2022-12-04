#Get data
with open('Year2022/Day4/Day4Input.txt') as f:
  pairs = f.read().strip().split("\n")
  
#print(pairs)

#Part 1
def part1():
  counta = 0
  countb = 0
  for pair in pairs:
    elf = pair.split(',')
    #print(elf)
    mid = [item.split(', ') for item in elf]
    elf1 = mid[0]
    elf2 = mid[1]
    
    #elf1 = elf1[start, finish] & elf2 = elf2[start, finish]
    s1 = [item.split('-') for item in elf1]
    s2 = [item.split('-') for item in elf2]
    elf1 = s1[0]
    elf2 = s2[0]

    #check if elf1 range is within elf2 range
    elf1s = int(elf1[0])
    elf1e = int(elf1[1])
    elf2s = int(elf2[0])
    elf2e = int(elf2[1])

    elf1_range = range(elf1s, elf1e+1)
    elf2_range = range(elf2s, elf2e+1)
    if int(elf2s) in elf1_range and int(elf2e) in elf1_range:

      counta +=1
    elif int(elf1s) in elf2_range and int(elf1e) in elf2_range:

      counta+=1
      
    #Part 2
    if elf2s in elf1_range or elf2e in elf1_range:
      countb+=1
    elif elf1s in elf2_range or elf1e in elf2_range:
      countb+=1

    
  print('Part 1 Answer:', counta)
  print('Part 2 Answer:', countb)


part1()