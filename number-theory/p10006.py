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

primes = set(fast_sieve_for_primes_to(65000))

def is_probably_prime(num):

  # return not any(not pow(a, num, num) == a for a in range(2, num))
  for a in range(2, num):
    if not pow(a, num, num) == a:
      return False
  return True
  
  
while True:
  num = int(input())
  if num == 0:
    break
  
  if not num in primes and is_probably_prime(num):
    print("The number {} is a Carmichael number.".format(num))
  else:
    print("{} is normal.".format(num))
