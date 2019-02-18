from sys import stdin, stdout

cases = int(stdin.readline().strip())

for c in range(cases):
  n = int(stdin.readline().strip())
  nums = list(map(int, stdin.readline().strip().split()))
  num_swaps = 0

  for i in range(n):
    for j in reversed(range(i+1, n)):
      if nums[j-1] > nums[j]:
        num_swaps += 1
        nums[j-1], nums[j] = nums[j], nums[j-1]
  
  stdout.write("Optimal train swapping takes {} swaps.\n".format(num_swaps))