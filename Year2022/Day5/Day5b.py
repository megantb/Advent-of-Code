#set variables
N = 9
drawing_lines = 8

#Get data
with open('Year2022/Day5/Day5Input.txt') as f:
  parts = f.read()[:-1].split("\n\n")
  drawing = parts[0].split('\n')
  stacks = [[] for _ in range(N)]

  for i in range(drawing_lines):
    line = drawing[i]
    crates = line[1::4]
    for s in range(len(crates)):
      if crates[s] != " ":
        stacks[s].append(crates[s])
#Reverse All stacks
stacks = [stack[::-1] for stack in stacks]

def part1():
  #Reverse All stacks
  #stacks = [stack[::-1] for stack in stacks]
  
  #Move things around
  for line in parts[1].split('\n'):
    tokens = line.split(" ")
    n, src, dst, = map(int, [tokens[1], tokens[3], tokens[5]])
    src -=1
    dst -=1
  
    for _ in range(n):
      pop = stacks[src].pop()
      stacks[dst].append(pop)
  
  tops = [stack[-1] for stack in stacks]
  return "".join(tops)

def part2():

  
  #Move things around
  for line in parts[1].split('\n'):
    tokens = line.split(" ")
    n, src, dst, = map(int, [tokens[1], tokens[3], tokens[5]])
    src -=1
    dst -=1
  
    stacks[dst].extend(stacks[src][-n:])
    stacks[src] = stacks[src][:-n]
  
  tops = [stack[-1] for stack in stacks]
  return "".join(tops)
  
print('Part 1: ', part1())
print('Part 2: ', part2())