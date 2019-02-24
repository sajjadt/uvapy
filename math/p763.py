from bisect import bisect_left

fib_numbers = [1, 2]
for i in range(100 + 10):
  fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

def from_fib(n):
  '''Converts Fibinary number n into integer'''
  res = 0
  for i, ch in enumerate(reversed(n)):
    if ch == "1":
      res += fib_numbers[i]
  return res

def to_fib(n):
  '''Converts integer n into sum of Fibonacci numbers using Greedy selection'''
  '''Refer to https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem'''
  factors = [] # position of 1s in fibinary number

  if n == 0:
    return "0"

  while n > 0:
    i = bisect_left(fib_numbers, n)
    if fib_numbers[i] == n:
      factors.append(i)
      n = 0
    else:
      factors.append(i-1)
      n -= fib_numbers[i-1]
  result = ["0"]*(max(factors) + 1)
  # Construct string representation
  for i in factors:
    result[i] = "1"
  return "".join(reversed(result))

from sys import stdin, stdout
case = 0
while True:
  line = stdin.readline()
  if line == "":
    break
  
  # Read two numbers
  line = line.strip()
  if line == "":
    line = stdin.readline()
  a = line.strip()
  b = stdin.readline().strip()

  total = from_fib(a) + from_fib(b)
  if case > 0:
    stdout.write("\n")
  stdout.write("{}\n".format(to_fib(total)))
  case += 1
