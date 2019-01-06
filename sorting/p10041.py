#!/usr/bin/python3

num_tests = int(input())
for i in range(num_tests):
  numbers = [int(x) for x in input().split()]
  count = numbers[0]

  locations = sorted(numbers[1:])
  median_index = count // 2
  distance = 0 

  times = 1
  for i in range(1, median_index+1):
    distance += times * (locations[i] - locations[i-1])
    times += 1 
  
  times = 1
  for i in range(count - 1, median_index, -1):
    distance += times * (locations[i] - locations[i-1])
    times += 1 
 
  print(distance)

