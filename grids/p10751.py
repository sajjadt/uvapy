from math import sqrt

num_cases = int(input())

diag_diff = sqrt(2) - 1

for t in range(num_cases):
  input()
  dim = int(input())

  if dim == 1:
    sol = 0
  else:
    sol = dim * dim 
    # number of diagonals steps
    # 1, 1-2-1, 1-2-3-2-1, 1-2-3-4-3-2-1 = (n - 2 )^2
    sol += ((dim-2)**2 * diag_diff)

  print("{:.3f}".format(sol))
  if t < num_cases - 1:
    print()