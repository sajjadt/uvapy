def my_pow(a, n, m):
  if n == 1:
    return a % m

  x = my_pow(a, n // 2, m) % m
  if n % 2 == 1:
    return (x * x * a) % m
  else:
    return x*x % m

from sys import stdin, stdout
cases = int(stdin.readline().strip())
for c in range(cases):
  x, y, z = list(map(int, stdin.readline().strip().split()))
  stdout.write("{}\n".format(my_pow(x, y, z)))
