#!/usr/bin/python3
while True:
  try:
    line = input()
    inps = list(map(int, line.split()))
    n = inps[0]
    covered = [False] * (n)

    if n < 2:
      print("Jolly")
      continue

    is_jolly = True
    for i in range(1, n):
      
      #if inps[i] <= 0 or inps[i+1] <= 0:
      #  is_jolly = False
      #  break 
      
      distance = abs(inps[i] - inps[i+1])

      if distance >= n:
        is_jolly = False
        break 
      
      if covered[distance]:
        is_jolly = False
        break

      covered[distance] = True
    print("Jolly" if is_jolly else "Not jolly")
  except EOFError:
    break

