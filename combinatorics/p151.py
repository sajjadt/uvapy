def josephus(n, k): 
  if (n == 1): 
    return 1
  else:
    return (josephus(n - 1, k) + k-1) % n  + 1

while True:
  n = int(input())
  if n == 0:
    break

  i = 1
  # 1 is the first one to shutoff power, so it is removed, and location 13 is now 12th location
  while josephus(n-1, i) != 12:
    i += 1
  print(i)
  