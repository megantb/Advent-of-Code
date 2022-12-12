with open("sample.txt") as fin:
  data = fin.read().strip().split('\n\n')
  #print(data)
  monkeys = {}
  mID = []
  mItem = []
  mItem2 = []
  mOp = []
  mTest = []
  mTrue = []
  mFalse = []
  mInsp = []
  mCount = []
  
data2 = [item.strip().split('\n') for item in data]
#print(data2)

for i in data2:
  
  #Monkey ID (mID)
  ID = i[0]
  ID2 = ID[-2]
  mID.append(ID2)
  monkeys['mID'] = mID
  mCount = 0
  monkeys['mCount'] = mCount
  #print(mID)

  #Monkey Items (mItem)
  ITEM = i[1]
  ITEM2 = ITEM[ITEM.find(":")+1:len(ITEM)]
  ITEM3 = ITEM2.split(',')
  mItem2 = []
  for j in ITEM3:
      j = j.strip()
      mItem2.append(j)
  mItem.append(tuple(mItem2))
  monkeys['mItem'] = mItem
#print(mID,'\n',mItem2)

  #Monkey Operation (mOp)
  OP = i[2]
  OP = OP[OP.find("old")+4:len(OP)]
  OP1, OP2 = OP.split(' ')
  mOp.append(tuple((OP1, OP2)))
  monkeys['mOp'] = mOp

  #Monkey Test (mTest)
  test = i[3]
  test2 = test[test.find("by")+3:len(test)]
  mTest.append(test2)
  monkeys['mTest'] = mTest

  #Monkey True (mTrue)
  True1 = i[4]
  True2 = True1[-1:]
  mTrue.append(True2)
  monkeys['mTrue'] = mTrue

  #Monkey False (mFalse)
  False1 = i[5]
  False2 = False1[-1:]
  mFalse.append(False2)
  monkeys['mFalse'] = mFalse


  
# print('mID: ', mID, '\n')
#print('mItem: ', mItem, '\n')
# print('mOp:', mOp, '\n')
# print('Test:', mTest, '\n')
# print('mTrue:', mTrue, '\n')
# print('mFalse:', mFalse, '\n')


#RUN THROUGH MONKEY INSPECTIONS
def monkey_insp(items):
  items = int(items)
  print('Monkey:', mID[ref])
  mOp1 = mOp[ref][0]
  mOp2 = mOp[ref][1]
  mTest1 = mTest[ref]
  mTrue1 = int(mTrue[ref])
  mFalse1 = int(mFalse[ref])
  mCount[ref] += 1
  
  if mOp2 == 'old':
    print(int(items))
    mOp3 = int(items)
  else:
    mOp3 = mOp2
    
  if mOp1 == '*':
    new = int(items) * int(mOp3)
    div = new//3
  elif mOp1 == "+":
    new = int(items) + int(mOp3)
  new = new//3
  
  div = int(mTest1)
  test = int(new%div)
  if test == 0:
    print('To Monkey:', mTrue1, '\n')
    newTuple = (new,)
    mItem[mTrue1]+= newTuple
    #print('New Item:', mItem[mTrue1])
  else:
    print('To Monkey:', mFalse1, '\n')
    newTuple = (new,)
    mItem[mFalse1] += newTuple
    #print('New Item:', mItem[mFalse1])
  
  
  return mCount
  

  
#loop through 20 times
# 1 round = 1 monkeys list of items
r=0
ref = 0
while r < 20:

  #Handle Monkey ID Reference
  mNum = len(mID)
  ref = r
  if ref >= mNum and ref < mNum*2:
    ref = ref - mNum
  elif ref >= mNum*2 and ref < mNum*3:
    ref = ref - mNum*2
  elif ref >= mNum*3 and ref < mNum*4:
    ref = ref - mNum*3
  elif ref >= mNum*4:
    ref = ref - mNum*4

  #Pass monkey and inspection items
  refItems = list(mItem[ref])
  print('Round:', r)
  
  items = map(monkey_insp, refItems)
  #print(list(items))
  print("mCount[0]:", mCount[0])

  r+=1  #Go to next round


  