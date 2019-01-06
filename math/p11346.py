from math import log

num_tests = int(input())
for test in range(num_tests):
  # Input is triple of real numbers
  a, b, S = list(map(float, input().split()))

  if a <= 0 or b <= 0 or S >= a*b:
    result = 0
  elif S == 0:
    result = 100
  else:
    # Calculate integral of S/x and how much it overlaps with [(0, 0) - (b, a)] rectangle
    result = a*b - S - S*log(a) + S*log(S) - S*log(b) 
    result *= 100 
    result /= (a*b)
  
  print ("{0:.6f}%".format(result))


