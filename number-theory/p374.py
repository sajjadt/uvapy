from time import time

def my_pow(a, n, m):
  if n == 1:
    return a % m

  x = my_pow(a, n // 2, m) % m
  if n % 2 == 1:
    return (x * x * a) % m
  else:
    return x*x % m

s = time()
while True:
  try:

    b = int(input())
    p = int(input())
    m = int(input())
    
    # Fast exponential
    # pow(b, p, m) works too
    print(my_pow(b, p, m) if p > 0 else 1)
    input()
  except(EOFError):
    break
e = time()
# print(e - s)