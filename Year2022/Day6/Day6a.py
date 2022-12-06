def check(data,n):    #pass data and 'n' number of distinct characters
    for i in range(len(data)-n):
        a = data[i:(i+n)]
        b = data[i+n]
        l = set([a.count(item) for item in a])
        if((l=={1}) and (b not in a)):
            return i+n+1

with open('Year2022/Day6/Day6Input.txt') as f:
    data = f.read()
    print('Part 1: ', check(data,3)) #Change 'n' 
    print('Part 2: ', check(data,13)) #Change 'n'

"""
s = data
n = size of message (remember count starts at 0)
  n = 1, char 2
  n = 3, char 4
"""