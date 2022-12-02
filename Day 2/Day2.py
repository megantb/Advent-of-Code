win = 6
draw = 3
loss = 0
TotalScoreA = 0
TotalScoreB = 0
rpts = 1
ppts = 2
spts = 3

file1 = open("Day2Input.txt", 'r')
lines = file1.readlines()

for line in lines:
  x,y=line.split();

  
  if x == "A":   #Opponent Plays Rock
    if y == "X":   #ROCK / LOSS
      TotalScoreA = TotalScoreA + draw + rpts  #rock/draw
      TotalScoreB = TotalScoreB + loss + spts  #rock/loss
    elif y == "Y":   #Paper / DRAW
      TotalScoreA = TotalScoreA + win + ppts  #paper/win
      TotalScoreB = TotalScoreB + draw + rpts  #paper/draw
    elif y == "Z":   #Scissors / WIN
      TotalScoreA = TotalScoreA + loss + spts  #Sc/loss
      TotalScoreB = TotalScoreB + win + ppts  #SC/win

  if x == "B":   #Opponent Plays Paper
    if y == "X":   #ROCK / LOSS
      TotalScoreA = TotalScoreA + loss + rpts  #rock/loss
      TotalScoreB = TotalScoreB + loss + rpts  #SC/loss
    elif y == "Y":   #Paper / DRAW
      TotalScoreA = TotalScoreA + draw + ppts  #paper/draw
      TotalScoreB = TotalScoreB + draw + ppts  #paper/draw
    elif y == "Z":   #Scissors / WIN
      TotalScoreA = TotalScoreA + win + spts  #Sc/win
      TotalScoreB = TotalScoreB + win + spts  #SC/win

  if x == "C":   #Opponent Plays Scissors
    if y == "X":   #ROCK / LOSS
      TotalScoreA = TotalScoreA + win + rpts  #rock/loss
      TotalScoreB = TotalScoreB + loss + ppts  #paper/loss
    elif y == "Y":   #Paper / DRAW
      TotalScoreA = TotalScoreA + loss + ppts  #paper/draw
      TotalScoreB = TotalScoreB + draw + spts  #sc/draw
    elif y == "Z":   #Scissors / WIN
      TotalScoreA = TotalScoreA + draw + spts  #Sc/win
      TotalScoreB = TotalScoreB + win + rpts  #rock/win



print(TotalScoreA)
print(TotalScoreB)