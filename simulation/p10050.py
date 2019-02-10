# Hartals

cases = int(input())

for c in range(cases):
  n = int(input())

  p = int(input())
  periods = []
  for i in range(p):
    periods.append(int(input()))

  # Have a boolean table to represetn hartal/non-hartal days
  is_hartal = [False]*(n+1)

  for p in periods:
    cp = p
    while cp <= n:
      if not is_hartal[cp]:
        mod = cp % 7
        if mod != 6 and mod != 0:
          is_hartal[cp] = True
      cp += p

  print(sum(is_hartal)) 
  
  
