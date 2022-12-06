# Open the input file in read-only mode
with open('Year2022/Day6/Day6Input.txt', 'r') as file:
    # Read the entire contents of the file
    data = file.read()

# Initialize a counter to keep track of how many characters have been processed
count = 0


def part1():


  # Initialize a counter to keep track of how many characters have been processed
  count = 0

  # Loop through each character in the data
  for c in data:
      # Increment the counter
      count += 1
  
      # Check if the current character, along with the previous three characters,
      # form a start-of-packet marker
      if len(set(data[count-4:count])) == 4:
          # If they do, print the number of characters that have been processed
          # and exit the loop
          #print(count)
          return count
          break


def part2():
  
  # Initialize a counter to keep track of how many characters have been processed
  count = 0
# Loop through each character in the data
  for c in data:
      # Increment the counter
      count += 1
  
      # Check if the current character, along with the previous three characters,
      # form a start-of-packet marker
      if len(set(data[count-14:count])) == 14:
          # If they do, print the number of characters that have been processed
          # and exit the loop
          #print(count)
          return count
          break

print("Part 1:", part1())
print("Part 2:", part2())