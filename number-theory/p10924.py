from string import ascii_letters

cost = {c:i+1 for i,c in enumerate(ascii_letters)}

def fast_sieve_for_primes_to(n):
  size = n//2
  sieve = [1]*size
  limit = int(n**0.5)
  for i in range(1,limit):
    if sieve[i]:
      val = 2*i+1
      tmp = ((size-1) - i)//val 
      sieve[i+val::val] = [0]*tmp
  return [1, 2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

sieve = set(fast_sieve_for_primes_to(1200))

while True:
  try:
    word = input().strip()
    val = sum(cost[c] for c in word)
    if val in sieve:
      print("It is a prime word.")
    else:
      print("It is not a prime word.")
  except(EOFError):
    break