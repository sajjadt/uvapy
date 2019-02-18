while True:
  a, b, c, d, e = list(map(int, input().split()))
  if a == b == c == d == e == 0:
    break
  
  # a,b,c ways to select (coat,hat,pant)
  # d**2 and e**2 to select socks and shoes
  print(a*b*c*(d**2)*(e**2))
