import numpy as np

with open('Year2022/Day8/Day8Input.txt') as f:
  data = f.read().strip().split('\n')
  
grid = [list(map(int, line)) for line in data]
x = len(grid)
y = len(grid[0])

grid = np.array(grid)

def part1():
  vis_trees = 0
  for r in range(x):
    for c in range(y):
      h_cur_tree = grid[r,c]
      
      if c == 0 or np.amax(grid[r, :c]) < h_cur_tree:  #looking left
        vis_trees +=1
      elif c == y-1 or np.amax(grid[r, (c+1):]) < h_cur_tree:  #looking right
        vis_trees +=1
      elif r == 0 or np.amax(grid[:r, c]) < h_cur_tree:  #looking up
        vis_trees +=1
      elif r == x-1 or np.amax(grid[(r+1):, c]) < h_cur_tree:
        vis_trees +=1

  return vis_trees
    


def part2():

  dir = [[0,1],[0,-1],[1,0], [-1,0]]  #right, left, up, down
  ans = 0
  for r in range(x):
    for c in range(y):
      h_cur_tree = grid[r,c]
      score = 1

      #look in all 4 directions
      for dirr, dirc in dir:
        rr, cc = r+dirr, c+dirc   #direction we are looking
        dist = 0
       

        while(0 <= rr < x and 0 <= cc < y) and grid[rr, cc]<h_cur_tree:    #row is between 0 & x AND column is between 0 and y
            dist += 1
            rr += dirr
            cc += dirc

            if (0 <= rr < x and 0 <= cc < y) and grid[rr, cc] >= h_cur_tree:
              dist += 1
            
        score *= dist
        #print(score)
      ans = max(ans, score)
  return ans

print("Part 1:", part1())
print("Part 2:", part2())