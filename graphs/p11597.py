# can always find N/2 subtrees formed by Euler tour in K(n) 
case = 1
while True:
  n = int(input())
  if n == 0:
    break
  print("Case {}: {}".format(case, n//2))
  case += 1