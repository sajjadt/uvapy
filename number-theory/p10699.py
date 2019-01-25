def get_primes(n):
  if n<=2:
    return []
  sieve=[True]*(n+1)
  for x in range(3,int(n**0.5)+1,2):
    for y in range(3,(n//x)+1,2):
      sieve[(x*y)]=False
  return [2]+[i for i in range(3,n,2) if sieve[i]]

def num_factors(n, primes):
  num = 0
  for candidate in primes:
    if candidate > n:
      break
    if n % candidate == 0:
      num += 1
    while n % candidate == 0:
      n = n // candidate
  if n != 1:
    return 1 + num
  else:
    return num

primes = get_primes(1001)

while True:
  n = int(input())
  if n == 0:
    break

  print("{} : {}".format(n, num_factors(n, primes)))