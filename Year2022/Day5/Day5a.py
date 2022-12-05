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
  print("".join(tops))