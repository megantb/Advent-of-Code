#Get Data
with open('Year2020/Day3/input.txt') as f:
  lines = f.read().strip().split("\n")
  grid = [list(line) for line in lines]
  x = len(grid)
  y = len(grid[0])
  #print(x, y)


def part1():
  #START
  r = 0
  c = 0
  tree_count = 0
  l = len(lines)
  for line in lines:
    #print(line)
    if c >= y:
      c = abs(y-c)
    for nr, nc in [(r, c)]:
      #print((nr, nc))
      #print(grid[nr][nc])
      if grid[nr][nc] == "#":
        tree_count +=1
      c += 3
      r += 1
  return tree_count


def part2():
  #START
  slopes = [(1,1), (1, 3), (1,5), (1,7), (2,1)]
  r = 0
  c = 0
  ans = 1
  tree_count = 0
  l = len(lines)
  y = len(grid[0])
  for slope in slopes:
      r = 0
      c = 0
      tree_count = 0
      sr = slope[0]
      sc = slope[1]
    
      #print(sr, sc)
      for line in lines:
          #print(line)
          if c >= y:
            c = abs(y-c)
          if r > x:
            break
          for nr, nc in [(r, c)]:
            print((nr, nc))
            #print(grid[nr][nc])
            if grid[nr][nc] == "#":
              tree_count +=1
            c += sc
            r += sr
      ans *= tree_count
      print(tree_count, sr, sc)
  return ans
  
print('Part 1:', part1())
print('Part 2:', part2())