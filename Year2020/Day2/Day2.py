#Get Data
with open('Year2020/Day2/Day2Input.txt') as f:
  data = f.read().strip().split("\n")
  data2 = [item.split(': ') for item in data]
  policies = [item[0] for item in data2]
  passwords = [item[1] for item in data2]

  policy = [item.split(' ') for item in policies]

#print('Policies: ', policies)
#print('Passwords: ',passwords)
#print('Policy: ', policy)

def part1():
  valid = 0
  for i in range(len(policy)):
    policy_param = policy[i]
    policy_start, policy_end = map(eval, policy_param[0].split('-'))
    policy_letter = policy_param[1]
    psw = passwords[i]
    #print(policy_start, policy_end, policy_letter, psw)
    if psw.count(policy_letter) >= policy_start and psw.count(policy_letter)<=policy_end:
        valid +=1
  return valid

def part2():
  valid = 0
  for i in range(len(policy)):
    policy_param = policy[i]
    policy_start, policy_end = map(eval, policy_param[0].split('-'))
    policy_letter = policy_param[1]
    psw = passwords[i]
    #print(policy_start, policy_end, policy_letter, psw)
    if psw[policy_start-1] == policy_letter and psw[policy_end-1]==policy_letter:
        continue 
    if psw[policy_start-1] == policy_letter and psw[policy_end-1]!=policy_letter:
        valid +=1
    if psw[policy_start-1] != policy_letter and psw[policy_end-1]==policy_letter:
        valid +=1
  return valid
print("Part 1: ", part1())
print("Part 2: ", part2())