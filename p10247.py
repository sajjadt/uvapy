from math import factorial

sol_space = {}

def foo(k, d):
  '''Recursive function to find number of valid expression with given length and depth'''
  global sol_space

  # invalid case
  if k <= 1 or d <= 0:
    return 1

  # Base cases
  if d == 0:
    return 1

  # Recursive cases
  # Check the solution space first
  if (k, d) in sol_space:
    return sol_space[(k, d)]
  
  num_nodes = int( (pow(k, d + 1) -1) / (k - 1)) - 1
  num_subgraph_nodes = num_nodes / k

  # Ways to pick up the root
  sol = 1

  # Ways to pick up the sub trees
  sol *= (factorial(num_nodes) // pow(factorial(num_subgraph_nodes), k))

  # Ways to form indvidiual subtress  
  sol *= pow(foo(k, d-1), k)

  return int(sol)

while True:
  try:
    k, d = list(map(int, input().split()))
    print(foo(k, d))
  except EOFError:
    break
  