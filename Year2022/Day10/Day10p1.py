
with open("Year2022/Day10/input.txt") as fin:
    lines = fin.read().split("\n")

x = 1    #initialize x
#set read points for answer
read_pts = [20, 60, 100, 140, 180, 220]
ans_array = []
ptindex = 0
cycle = 0    #initialize cycle
ans =0       

for line in lines:    #loop through each line
  #cycle += 1
  if line == "noop":  #if noop, increase cycle by 1
    cycle +=1
    
    if cycle in read_pts:
      pt_ans = cycle * x
      ans_array.append([x, cycle])
      ans += cycle * x
      ptindex +=1
      #print (ans_array)
  else:
    instr = line.split(' ')
    V = int(instr[1])
    x += V
    cycle += 1
    
    if cycle in read_pts:
      ans_array.append([(x-V), cycle])
      ans += cycle * (x-V)
      ptindex +=1
      #print (ans_array)

    cycle += 1

    if cycle in read_pts:
      ans_array.append([(x-V), cycle])
      ans += cycle * (x-V)
      ptindex +=1
      #print (ans_array)

print(ans_array)
#for i in range(len(ans_array)):
  #a = ans_array[i,0]
 # b = ans_array[0,i]
  #print (a*b)
  
print(ans)
    