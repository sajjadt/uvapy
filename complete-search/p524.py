def prime_ring_formatinos(n):
  
  # Initial Arrangement
  arrangements = [i+1 for i in range(n)]
  is_prime = [True if i in set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) else False for i in range(32)]
  numbers_used = [False] * (n+1)

  def form_ring(i):
    if i == n:
      if is_prime[arrangements[0] + arrangements[-1]]:
        yield arrangements
    else:
      for j in range(2, n+1):
        if not numbers_used[j]:
          total = j + arrangements[i-1]
          if is_prime[total] :
            numbers_used[j] = True
            arrangements[i] = j
            yield from form_ring(i+1)
            numbers_used[j] = False
    
  numbers_used[1] = True
  yield from form_ring(1)

# import time
from sys import stdout
# st = time.time()

test_case = 1
while True:
  try:
    n = int(input())
    forms = []

    if test_case > 1:
      print()
    
    print("Case {}:".format(test_case))

    for form in prime_ring_formatinos(n):
      stdout.write(" ".join(map(str, form))+"\n")

    test_case += 1
  except(EOFError):
    break
# et = time.time()
# print(et - st)