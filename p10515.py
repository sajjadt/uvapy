

def pow_10(m, n):

  m = int(m[-1])
  n = int(n[-2:])
  
  table = {0, 1, 5, 6}
  if n == 0:
    res = 1
  elif m in table:
    res = m
  elif m == 2:
    res = [6, 2, 4, 8][n%4]
  elif m == 3:
    res = [1, 3, 9, 7][n%4]
  elif m == 4:
    res = [6, 4][n%2]
  elif m == 7:
    res = [1, 7, 9, 3][n%4]
  elif m == 8:
    res = [6, 8, 4, 2][n%4]
  else:  # m = 9
    res = [1, 9][n%2]
  return res

while True:
  m, n = list(map(str, input().split()))
  
  if m == n == "0":
    break

  print(pow(int(m), int(n), 10))


