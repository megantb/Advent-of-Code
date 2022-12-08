#import numpy as np

with open('Year2022/Day8/Day8Sample.txt') as f:
  data = f.read().strip().split('\n')
  
grid = [list(map(int, line)) for line in data]
x = len(grid)
y = len(grid[0])

vis_trees = 0

def part1():

  for r in range(x):
    for c in range(y):
      h_cur_tree = grid[r][c]
      
      if c == 0 or np.amax(grid[r, :c]) < h_cur_tree:  #looking left
        vis_trees +=1
      elif c == y-1 or np.amax(grid[r, (c+1):]) < h_cur_trees:  #looking right
        vis_trees +=1
      elif r == 0 or np.amax(grid[:r, c]) < h_cur_tree:  #looking up
        vis_trees +=1
      elif r == x-1 or np.amax(grid[(r+1):, c]) < h_cr_tree:
        vis_trees +=1

  return vis_trees
    


#def part2():

  

print("Part 1:", part1())
#print("Part 2:", part2())