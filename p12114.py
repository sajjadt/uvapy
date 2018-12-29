

case = 1
while True:
  B, S = list(map(int, input().split()))
  if B == 0 and S == 0:
    break

  if B == 1:
    print("Case " + str(case) +": :-\\")
  elif S >= B:
    print("Case " + str(case) +": :-|")
  else:
    print("Case " + str(case) +": :-(")
  
  
  case += 1