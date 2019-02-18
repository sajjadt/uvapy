from sys import stdin, stdout

while True:
  a, b, c, d, l = list(map(int, stdin.readline().strip().split()))
  
  if a == b == c == d == l:
    break
  
  sol = 0
  # L < 1000
  for x in range(l+1):
    if (x*(a*x + b) + c) % d == 0:
      sol += 1
  
  stdout.write("{}\n".format(sol))