from bisect import bisect_left 
  
def binary_search(a, x): 
  i = bisect_left(a, x) 
  if i != len(a) and a[i] == x: 
    return i 
  else: 
    return -1

# def fast_primes(n):
#   size = n//2
#   sieve = [1]*size
#   limit = int(n**0.5)
#   for i in range(1,limit):
#     if sieve[i]:
#       val = 2*i+1
#       tmp = ((size-1) - i)//val 
#       sieve[i+val::val] = [0]*tmp
#   return [2] + [i for i, v in enumerate(sieve) if v and i>2]

def fast_sieve_for_primes_to(n):
  size = n//2
  sieve = [1]*size
  limit = int(n**0.5)
  for i in range(1,limit):
    if sieve[i]:
      val = 2*i+1
      tmp = ((size-1) - i)//val 
      sieve[i+val::val] = [0]*tmp
  return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]


sieve = fast_sieve_for_primes_to(2**15)
while True:
  n = int(input())

  if n == 0:
    break

  half_n = n // 2
  sol = 0
  for i, prime in enumerate(sieve):
    if prime > half_n:
      break
    if binary_search(sieve, n - prime) != -1:
      sol += 1
  
  print(sol)
