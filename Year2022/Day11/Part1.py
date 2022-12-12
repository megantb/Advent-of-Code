with open("sample.txt") as fin:
  monkey_data = fin.read().strip().split('\n\n')

monkeys = []

#***************MONKEY MATH**********************
def monkey_math(mOp, oitem):
  l, op, mod1 = mOp

  if op == "+":
    return oitem + int(mod1)
  else:
    if mod1 == "old":
      return oitem * oitem
    else:
      return oitem * int(mod1)
      
  

#*************************MONKEY CLASS***************************
class Monkey:
  def __init__(self, items, operation, test):
    self.items = items
    #print(self.items)
    self.operation = operation
    self.test = test
    self.inspections = 0
    
    def __str__(self):
            return f"{self.items}, {self.operation}, {self.test}"
#*************************MONKEY CLASS***************************
      
lines = [item.strip().split('\n') for item in monkey_data]  

for i in lines:
  
  #Monkey ID
  ID = i[0]
  mID = ID[-2]

  #Monkey Items
  ITEM = i[1]
  ITEM2 = ITEM[ITEM.find(":")+1:len(ITEM)]
  ITEM3 = ITEM2.split(',')
  mItem2 = []
  for j in ITEM3:
      j = int(j.strip())
      mItem2.append(j)
  mItems = mItem2
  
  #Monkey Test
  test = i[3]
  mTest = test[test.find("by")+3:len(test)]

  #Monkey Operation (mOp)
  OP = i[2]
  mOp = i[2][2:].split(" ", 3)[3].split(" ")
  #op, mMod = mOp.split(' ')

  #Monkey True (mTrue)
  True1 = i[4]
  mTrue = int(True1[-1:])

  #Monkey False (mFalse)
  False1 = i[5]
  mFalse = int(False1[-1:])

  #Create Monkey
  monkeys.append(Monkey(mItems, mOp,[mTest, mTrue, mFalse]))


#loop through 20 times
# 1 round = 1 monkeys list of items
r=0
mNum = len(monkeys)
for r in range(0,10000):
  for ref in range(mNum):
    monkey = monkeys[ref]
    for item in monkey.items:
      item = monkey_math(monkey.operation, item)
      item = int(item)
      #item //= 3

      mTest, mTrue, mFalse = monkey.test
      mod = int(mTest)
      item = int(item)
      if item % mod == 0:
        monkeys[mTrue].items.append(item)
      else:
        monkeys[mFalse].items.append(item)

      monkey.inspections += 1

    #Empty monkey's items
    monkey.items = []

#Part 1 Answer
mAmounts = [m.inspections for m in monkeys]
mSorted = sorted(mAmounts)
print(mSorted[-1]*mSorted[-2])
      
        

  
  