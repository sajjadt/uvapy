from math import log10, floor, factorial

while True:
  try:
    n, k = list(map(int, input().split()))

    if k > n - k:
      k = n - k

    s = sum([log10(i) for i in range(1, k+1, 1)]) 
    p = sum([log10(i) for i in range(n-k+1, n+1, 1)])
    print(floor(p-s)+1)

    # print()

  except(EOFError):
    break