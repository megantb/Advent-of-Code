#Get data
with open('Year2021/Day4/Day4Input.txt') as f:
  #data = [i for i in f.read().strip().split("\n")]
  numbers, *boards = f.read().split('\n\n')
  numbers = [int(i) for i in numbers.split(',')]
  allBoards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]
#print(numbers)
#print(allBoards)

# Place an 'x' if a number in the board is called
def mark_board(number, board):
  for row in board:
    for col in range(0, len(row)):
      if row[col] == number:
        row[col] ='x'

# Sum all numbers on board which are not an 'x'
def sum_board(board):
  sum = 0
  for row in board:
    for num in row:
      if num != 'x':
        sum += num
  return sum


#Check if there is a winner
def check_for_win(board):
  winner = False

  #Check rows
  for row in board:
    winner = all(elem in ['x'] for elem in row)
    if winner:
      return winner

  #check columns
  for col in range(0,5):
    winner = all(elem in ['x'] for elem in [row[col] for row in board])
    if winner:
      return winner

  return winner

# Part 1
def part1():
  boards = allBoards

  for number in numbers:  #Start calling numbers
    for board in boards:  
      mark_board(number, board)  #if you have the number, mark it on your board  
      if check_for_win(board):  #see if a winner is found
        return sum_board(board) * number  


# Part 2
def part2():
  boards = allBoards
  allNums = numbers

  winnerFound = False
  while not winnerFound:
    number = allNums[0]  #every time while loop runs, and new number is called
    allNums = allNums[1:]  #every time while loop runs, allNums becomes shorter

    for board in boards:
      mark_board(number, board)

    #see if there is a winning board
    #index boards and delete if winner
    index = 0
    while index < len(boards):
      if check_for_win(boards[index]):
        if len(boards)>1:
          boards.pop(index)
        else:
          #if list is just 1
          winnerFound = True
          return sum_board(boards[index])*number
      else:    #no winner found
        index +=1


  
print("Part 1 Answer: ", part1())
print("Part 2 Answer: ", part2())