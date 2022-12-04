#Get Data
with open('Year2021/Day1/Day1Input.txt') as f:
  data = [int(i) for i in f.read().strip().split("\n")]

#print(data)

#Part 1
def part1():
  result = [firstnum < secondnum for firstnum, secondnum in zip(data, data[1:])]
  return sum(result)

#Part 2
def part2():
  allsum = [sum(mytuple) for mytuple in zip(data, data[1:],data[2:])]
  result = [firstsum < secondsum for firstsum, secondsum in zip(allsum, allsum[1:])]
  return sum(result)

print("Part 1 Answer:", part1())
print("Part 2 Answer:", part2())
    