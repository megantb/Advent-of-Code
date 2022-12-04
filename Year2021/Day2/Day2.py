#Get Data
with open('Year2021/Day2/Day2Input.txt') as f:
  data = [i for i in f.read().strip().split("\n")]
#print(data)

#Part 1
def part1():
  horiz = 0
  depth = 0

  for i in data:
    l=len(i)
    direction = i[0]
    units = i[-1]

    if direction == 'f':
      horiz += int(units)
    elif direction == 'd':
      depth += int(units)
    elif direction == 'u':
      depth -= int(units)

  return horiz*depth

#Part 2
def part2():
  horiz = 0
  depth = 0
  aim = 0

  for i in data:
    l=len(i)
    direction = i[0]
    units = i[-1]

    if direction == 'f':
      horiz += int(units)
      depth += aim * int(units)
    elif direction == 'd':
      #depth += int(units)
      aim += int(units)
    elif direction == 'u':
      #depth -= int(units)
      aim -= int(units)

  return horiz*depth
  
print("Part 1 Answer: ", part1())
print("Part 2 Answer: ", part2())

  