import collections 
from random import random 

def prime_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return factors

while True:
  try:
    n, m = list(map(int, input().split()))

    # M Factorization
    factors = collections.Counter(prime_factors(m))
    max_fact = 0

    
    divides = True
    for prime, freq in factors.items():
      # Count if there is at least freq occurnace of prime in factorization of n!
      t_freq = 0
      temp = prime
      while n >= temp:
        t_freq += n // temp
        temp = temp * prime
      if t_freq < freq:
        divides = False
        break

    if not divides:
      print("{} does not divide {}!".format(m, n))
    else:
      print("{} divides {}!".format(m, n))
       

  except(EOFError):
    break
