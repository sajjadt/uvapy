
while True:
  n, d = list(map(int, input().split()))

  if n == d == 0:
    break

  # N ways to give away each CD
  print(pow(n, d))