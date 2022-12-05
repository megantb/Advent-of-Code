#Get Data
with open('Year2020/Day2/Day2Sample.txt') as f:
  data = f.read().strip().split("\n")
  data2 = [item.split(': ') for item in data]
  policies = [item[0] for item in data2]
  passwords = [item[1] for item in data2]

  policy = [item.split(' ') for item in policies]
  #print(policy)
#print(data2)
print('Policies: ', policies)
print('Passwords: ',passwords)
print('Policy: ', policy)

def part1():
  policy_start = [item.split('-') for item in policy]
  print(policy_start)
#  for password in passwords:
#    if 
  pass
print("Part 1: ", part1())