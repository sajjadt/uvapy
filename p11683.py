
while True:
  h, w = list(map(int, input().split()))
  if h == w == 0:
    break

  block = list(map(int, input().split()))
  block.append(h)

  sol = 0
  for i in range(len(block)-1):
    if block[i+1] > block[i]:
      sol += (block[i+1] - block[i])

  print(sol)