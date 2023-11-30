with open("Year2022/Day13/Day13input.txt") as fin:
    pairs = fin.read().split("\n\n")

rcount = 0  #part 1 answer

#COMPARE PACKET TYPES
def compare(l,r):
  if type(l)==int and type(r)==list:    #convert the int to list if not same
    l = [l]
    print('Convert l:',l, r)
  if type(l)==list and type(r)==int:    #convert the int to list if not same
    r = [r]
    print('Convert r:',l,r)
 
  if type(l)==int and type(r)==int:    #Compare if both are INT
    if l<r:                            #If left is less than right
      print('True l<r:', l, r)
      return True
    if l==r:
      print('False l=r:', l, r)
      return False
    print('False l<r:', l, r)
    return 'No'
    
  #Compare if both are LIST
  if type(l)==list and type(r)==list:    
    i=0
    j=0
    llen = len(l)
    rlen = len(r)
    
    for i,j in zip(range(llen), range(rlen)):
      #print('In the List Section')
      c =  compare(l[i], r[j])
      if c == True:
        print('True c',l[i], r[j] )
        return True
      if c=='No':
        print('False c',l[i], r[j])
        return 'No'
        break
      if i ==llen:
        break
      i +=1
      j +=1
      
    
    if i==llen:
      if llen == rlen:
        print('False lenl=lenr:', llen, rlen)
        return False
      return True
    return 'No'

  # return False
        
    
  

#MAIN CODE
for i, packet in enumerate(pairs):
    l, r = map(eval, packet.split('\n'))
    print('\n**********\nPair:', i+1)
    # print('Packet:\n',packet,'\n...........')
    if compare(l,r) == True:
      rcount += i+1
      print('\nRound Count:', rcount)
print('\n\n\n\nPart 1 Answer:', rcount)
  