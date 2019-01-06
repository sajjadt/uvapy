

sol_space = {}
def foo(n, d):
  '''Recursive function to find number of valid expression with given length and depth'''
  global sol_space

  if n ==0 and d == 0:
    return 1
    
  # invalid cases
  if n < 2*d:
    return 0
  
  if n % 2 == 1:
    return 0

  if n == 0 or d == 0:
    return 0

  # Base cases
  if n == 2*d :
    return 1    
  
  if d == 1:
    return 1

  # Recursive cases
  # Check the solution space first
  if (n, d) in sol_space:
    return sol_space[(n, d)]
  
  sol = 0
  # (d-1) case
  sol += foo(n-2, d-1)
  # U*V case : d.d, 2 d.d-1, ..., 2 d.1
  for i in range(2, n, 2): # i = left block size from [2 to n-2]
    for j in range(0, d): # 
      sol += foo(i, d)*foo(n-i, j)
    #sol += foo(i-2, d-1)*foo(n-i-2, d-1)
    # if (n, d) == (8, 2):
    #   print(" - ", (i, d), "*", (n-i, d))
    #sol += 2*foo(i-2, d-1)*foo(n-i-2, d-1)

  # Update the solution space
  sol_space[(n, d)] = sol 
  return sol

while True:
  try:
    n, d = list(map(int, input().split()))
    print(foo(n, d) if n % 2 == 0 else 0)
  except EOFError:
    break
  