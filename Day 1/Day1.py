with open("Day1Input.txt", 'r') as f:
    elves = [x.split('\n') for x in f.read().split("\n\n")]

cals = sorted([sum([int(x) for x in y if x.isdigit()]) for y in elves])

print(max(cals))
print(sum(cals[-3:]))