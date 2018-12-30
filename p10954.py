from heapq import heappush, heappop, heapify

while True:
  num_numbers = int(input())

  if num_numbers == 0:
    break
  
  numbers = list(map(int, input().split()))
  
  sol = 0
  if num_numbers >= 2:
    heapify(numbers)
    sol = partial_sum = heappop(numbers) + heappop(numbers)
    for j in range(num_numbers - 2) :
      heappush(numbers, partial_sum)
      partial_sum = heappop(numbers) + heappop(numbers)
      sol += partial_sum
  
  print(sol)
