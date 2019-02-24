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

from bisect import bisect_left 
def binary_search(a, x): 
  i = bisect_left(a, x) 
  if i != len(a) and a[i] == x: 
    return i 
  else: 
    return -1

sieve = set(fast_sieve_for_primes_to(1000000+1))

from sys import stdin, stdout
while True:
  line = stdin.readline()
  if line == "":
    break
  line = line.strip()
  
  n = int(line)

  # Using sorted array to store prime numbers
  # if binary_search(sieve, n) == -1:
  #   stdout.write("{} is not prime.\n".format(n))
  # else:
  #   n_reversed = int(line[::-1])
  #   if n == n_reversed or binary_search(sieve, n_reversed) == -1:
  #     stdout.write("{} is prime.\n".format(n))
  #   else:
  #     stdout.write("{} is emirp.\n".format(n))

  # Using set to store prime numbers 
  if not n in sieve:
    stdout.write("{} is not prime.\n".format(n))
  else:
    n_reversed = int(line[::-1])
    if n == n_reversed or not n_reversed in sieve:
      stdout.write("{} is prime.\n".format(n))
    else:
      stdout.write("{} is emirp.\n".format(n))


