
sol_space = {}
def foo(n):
  global sol_space

  if n < 1:
    return 1

  # Check out the solution space first
  if n in sol_space:
    return sol_space[n]
  
  sol = 0
  if n >= 1:
    sol += 2 * foo(n - 1) 
  if n >= 2:
    sol += foo(n - 2)
  if n >= 3:
    sol += foo(n - 3)
  
  # Update solution space
  sol_space[n] = sol
  return sol

while True:
  try:
    number = int(input())
    print(foo(number))
  except EOFError:
    break
  