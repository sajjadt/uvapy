while True:
  n = int(input())

  if n < 0:
    break
  else:
    res = ""
    while n >= 3:
      n, r = divmod(n, 3)
      res += str(r)
    res += str(n)
    res = res[::-1]
    print(res)
