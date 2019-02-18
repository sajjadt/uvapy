from math import pow

while True:
  h0, num_workers = list(map(int, input().split()))

  if h0 == num_workers == 0:
    break

  if h0 == num_workers:
    v1, v2 = 0, h0
  else:
    N = -1
    for k in range(1, 32):

      n = pow(num_workers, 1/k)
      N = int(n)
      
      if N**k == num_workers:
        if (N+1)**k == h0:
          break
      elif (N+1)**k == num_workers:
        if (N+2)**k == h0:
          N = N + 1
          break
      elif (N-1)**k == num_workers:
        if (N)**k == h0:
          N = N-1
          break

    v1 = sum(N**i for i in range(k))
    v2 = sum( (h0 // ((N+1)**i))*(N)**i for i in range(k+1))
  print(v1, v2)