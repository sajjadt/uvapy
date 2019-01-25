from time import time
def fast_primes(n):
  # n = 18500000
  size = n//2
  sieve = [1]*size
  limit = int(n**0.5)
  for i in range(1,limit):
    if sieve[i]:
      val = 2*i+1
      tmp = ((size-1) - i)//val 
      sieve[i+val::val] = [0]*tmp
  return [2] + [i for i, v in enumerate(sieve) if v and i>0]

primes = fast_primes(18500000)

twins = [0]*(2**17)
j = 0
for i in range(len(primes)-1):
  tmp = primes[i]
  if tmp + 1 == primes[i+1]:
    twins[j] = (2*tmp+1, 2*tmp+3)
    j += 1

while True:
  try:
    n = int(input())
    print(twins[n-1])
  except(EOFError):
    break
