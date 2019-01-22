from sys import stdin, stdout
while True:
  n, m, c = list(map(int, stdin.readline().strip().split()))
  if n == m == c == 0:
    break
  
  sol = (n-7) * (m-7) // 2
  if n % 2 == 0 and m % 2 == 0 and c == 1:
    sol += 1
  stdout.write("{}\n".format(sol))