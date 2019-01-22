# 11581 Grid Successors
from sys import stdin

num_cases = int(input())

# Simulation
for t in range(num_cases):
  input()
  numbers = list(map(int, list(stdin.readline().strip())))
  numbers += list(map(int, list(stdin.readline().strip())))
  numbers += list(map(int, list(stdin.readline().strip())))

  next_numbers = [0] * 9
  steps = 0
  while any(numbers):
    next_numbers = [
      numbers[1] ^ numbers[3],
      numbers[0] ^ numbers[2] ^ numbers[4],
      numbers[1] ^ numbers[5],
      numbers[0] ^ numbers[4] ^ numbers[6],
      numbers[1] ^ numbers[3] ^ numbers[5] ^ numbers[7],
      numbers[2] ^ numbers[4] ^ numbers[8],
      numbers[3] ^ numbers[7],
      numbers[4] ^ numbers[6] ^ numbers[8],
      numbers[5] ^ numbers[7],
    ]  
    numbers = next_numbers
    steps += 1
  
  print(steps-1)