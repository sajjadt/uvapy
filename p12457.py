
sol_space = {}
def foo(num_matches, matches_to_win, p):
  global sol_space

  if num_matches < matches_to_win:
    return p
  
  if num_matches == matches_to_win:
    return pow(p, num_matches)

  if (num_matches, matches_to_win) in sol_space:
    return sol_space[(num_matches, matches_to_win)]

  if matches_to_win == 0:
    return 1

  sol = p * foo(num_matches-1, matches_to_win - 1, p) + (1 - p)* foo(num_matches-1, matches_to_win, p)
  sol_space[(num_matches, matches_to_win)] = sol
  return sol


num_tests = int(input())
for test in range(num_tests):
  n = int(input())
  p = float(input())

  sol_space.clear()
  sol = foo(2*n - 1, n, p)
  print("{0:.2f}".format(sol))


