from sys import stdin, stdout

def choose(n, k):
  if k == n: return 1
  if k > n: return 0
  d, q = max(k, n-k), min(k, n-k)
  num =  1
  for n in range(d+1, n+1): num *= n
  denom = 1
  for d in range(1, q+1): denom *= d
  return num // denom

cases = int(stdin.readline().strip())

for c in range(cases):
  numbers = list(map(int, stdin.readline().strip().split()))

  n = numbers[0]
  k = numbers[1]

  # append a block to each strip (right side) to make sure they wont touch eachother
  stripes = sum(numbers[2:]) + k - 1
  
  stdout.write("{}\n".format(choose(n - stripes + k, k)))
