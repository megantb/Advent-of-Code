with open("Year2022/Day14/sample.txt") as fin:
    input_list = fin.read().split("\n")

# Split the input strings and extract the coordinates
split_list = [[[int(x.strip()) for x in y.split(',')] for y in z.split('->')] for z in input_list]
#print(split_list)
#print(len(split_list[1]))
coordinates = [x for sublist in split_list for x in sublist]

rock = set()

# Find the min and max x and y coordinates
min_x = min([x[0] for x in coordinates])
max_x = max([x[0] for x in coordinates])
min_y = 0 #min([x[1] for x in coordinates])
max_y = max([x[1] for x in coordinates])

# Create a grid of . characters with the appropriate dimensions
grid = [['.' for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]

# Mark the coordinates with # characters
#for lines in split_list:
p = 1
for line in split_list:
  l = len(line)
  #print('\n NEW LINE', l)
  for coordinate in line[:l-1]:
    p1 = coordinate
    p2 = coordinates[p]
    #print('S:',coordinate)
    #print("E:", p2)

    x, y = coordinate
    x2, y2 = p2
    
    grid[y - min_y][x - min_x] = '#'      #start point
    grid[y2 -min_y][x2 - min_x] = "#"     #end point
    rock.add((x,y))
    rock.add((x2,y2))
    #determine which direction to move (R/D) and plot those points
    if abs(x-x2) >0:
      for i in range(x2, x):
        #print('x middle pt:',i,y)
        grid[y - min_y][i - min_x] = '#'
        rock.add((i,y))
    if abs(y-y2) >0:
      for j in range(y, y2):
        #print('y middle pt:',x,j)
        grid[j - min_y][x - min_x] = '#' 
        rock.add((x,j))
    p+=1

  p+=1
# Print the grid
for row in grid:
    print(' '.join(row))

print(rock)

#ENTER THE SANDMAN
sand_start = (500,0)

max_y = max([coordinate[1] for coordinate in rock])


def sandman():
  global rock
  sx = 500
  sy = 0

  while sy <= max_y:
      if(sx, sy+1) not in rock:    #down
          sy+=1
          #print('moved down', sandcount)
          continue
  
      if(sx-1, sy+1) not in rock:  #down and left
          sy+=1
          sx-=1
          #print('moved down & left', sandcount)
          continue 
  
      if(sx+1, sy+1) not in rock:  #down and right
          sy+=1
          sx+=1
          #print('moved down & left', sandcount)
          continue 
  
      #Add coordinates where the sand landed
      rock.add((sx,sy))
      return True
    
  return False

sandcount = 0

while True:
  sand = sandman()

  if not sand:
    break 

  sandcount +=1

print('Part 1:', sandcount)


    
    
    
  