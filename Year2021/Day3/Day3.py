#Get data
with open('Year2021/Day3/Day3Input.txt') as f:
  data = [i for i in f.read().strip().split("\n")]
#print(data)

#Binary to Integer (Decimal) function
def binary_to_int(binaryString):
  return int(binaryString, 2)
  
#Part 1
def part1():
  gamma = []  #make a list to store binary
  epsi = []   #make a list to store binary

  for column in range(0,len(data[0])):
    zeros = 0
    ones = 0

    for bits in data:
      if bits[column] =='0':
        zeros += 1
      else:
        ones += 1
    #print('zeros:', zeros)
    #print('ones: ', ones)

    if zeros > ones:
      gamma.append('0')
      epsi.append('1')
    elif zeros < ones:
      gamma.append('1')
      epsi.append('0')
  
  #print('Gamma Rate: ', gamma)
  #print('Epsilon Rate: ', epsi)

  gamma = ''.join(gamma)
  epsi = ''.join(epsi)
  
  powerConsumption = binary_to_int(gamma) * binary_to_int(epsi)

  return powerConsumption
  
#Part 2
def part2():

  firstData = data.copy()
  
  #finding oxygen reading
  i = 0
  while len(firstData)>1:
    zeros = 0
    ones = 0

    #counter
    for bits in firstData:
      if bits[i] =='0':
        zeros += 1
      else:
        ones += 1

    #Shorten the list
    if zeros > ones:
        firstData = [bits for bits in firstData if bits[i]=='0']
    else:
       firstData = [bits for bits in firstData if bits[i]=='1']
    
    i += 1

  oxyRate = ''.join(firstData)  
  
  #Second Data - CO2 Reading
  secondData = data.copy()
  i=0
  while len(secondData)>1:
      zeros = 0
      ones = 0
  
      #counter
      for bits in secondData:
        if bits[i] =='0':
          zeros += 1
        else:
          ones += 1
  
      #Shorten the list
      if zeros > ones:
          secondData = [bits for bits in secondData if bits[i]=='1']
      else:
         secondData = [bits for bits in secondData if bits[i]=='0']
      i += 1
  coRate = ''.join(secondData)

  supportRating = binary_to_int(oxyRate) * binary_to_int(coRate)
  return supportRating

print("Part 1 Answer: ", part1())
print("Part 2 Answer: ", part2())