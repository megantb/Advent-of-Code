#REFERENCE
#https://www.redblobgames.com/pathfinding/grids/graphs.html
from string import ascii_lowercase

with open("Year2022/Day12/Day12sample.txt") as fin:
    lines = fin.read().split("\n")
    grid = [list(line) for line in lines]
    x = len(grid)
    y = len(grid[0])
  
all_nodes = []

#FIND START AND END POINTS (NODES)
for i in range(x):
  for j in range(y):
    c = grid[i][j]
    all_nodes.append([i,j])
    if c == "S":    #Find start point coordinates
      start = i, j
    elif c == "E":  #Find end point coordinates
      end = i, j
print('Start Point:',start)
print('End Point:',end,'\n')


#The edges are going to be the four directions: east, north, west, south
def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ox = node[0]
    oy = node[1]
    opt = grid[ox][oy]
    result = []
    cresult = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in all_nodes:
            nx = neighbor[0]
            ny = neighbor[1]
            npt = grid[nx][ny]
            if getptheight(npt) <= getptheight(opt):
              print(npt)
            result.append(neighbor)  
    return result
    

def getptheight(p):
  if p in ascii_lowercase:
    return ascii_lowercase.index(p)
  elif p == "S":
    return 0
  elif p == "E":
    return 25

for a in range(x):
  for b in range(y):
    p = (a,b)
    l = grid[a][b]
    
    print('Point:', p)
    print('Value:', l)
    #print('Height:', getptheight(l))
    print('Neighbors:',neighbors(p), '\n')
    
