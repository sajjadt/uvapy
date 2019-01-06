def choose(n, k):
  if k == n: return 1
  if k > n: return 0
  d, q = max(k, n-k), min(k, n-k)
  num =  1
  for n in range(d+1, n+1): num *= n
  denom = 1
  for d in range(1, q+1): denom *= d
  return num // denom

num_tests = int(input())
sol_space = [1, 1, 2, 4]
for test in range(num_tests):
  num = int(input())
  
  if num > 3:
    # 1 land
    sol = 1

    # 1 new land per each pair
    sol += choose(num, 2)
    
    # new land per each four points (not covered by previous case) 
    #   ----
    #  | \  |
    #  |  \ |
    #   ----
    sol += choose(num, 4) 
  elif num >= 0:
    sol = sol_space[num]
  else:
    sol = 0
  
  print(int(sol))

