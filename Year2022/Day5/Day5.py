
stacks = [[]]
#Get data
with open('Year2022/Day5/Day5Sample.txt') as f:
  stacks, moves = f.read().split('\n\n')


    
  for line in moves.split('\n'):
      instr = line.split(" ")
      amt, frm, to = map(int, [instr[1], instr[3], instr[5]])
      frm -=1
      to -=1
 

    