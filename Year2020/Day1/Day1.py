#Get Data
with open('Year2020/Day1/Day1Input.txt') as f:
  data = [int(i) for i in f.read().strip().split("\n")]

def part1():

  for x in data:
    for y in data:
      if x+y == 2020:
        return (x*y)

def part2():
    for x in data:
      for y in data:
        for z in data:
          if x+y+z == 2020:
            return (x*y*z)

print('Part 1 Answer: ', part1())
print('Part 2 Answer: ', part2())