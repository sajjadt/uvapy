from sys import stdin, stdout

while True:
  n, m = list(map(int, stdin.readline().strip().split()))

  if n == m == 0:
    break
  
  heads = []
  knights = []

  for i in range(n):
    heads.append(int(stdin.readline().strip()))
  for i in range(m):
    knights.append(int(stdin.readline().strip()))
  
  if len(heads) > len(knights):
    print("Loowater is doomed!")
  else:
    # In-place sort
    heads.sort()
    knights.sort()

    cost = 0
    # Start matching from left to find the optimum matching
    i = 0
    j = 0
    while i < len(heads) and j < len(knights) and len(heads) - i <= len(knights) - j:
      if heads[i] <= knights[j]:
        cost += knights[j]
        i += 1
      j += 1

    if i == len(heads):
      stdout.write("{}\n".format(cost))
    else:
      stdout.write("Loowater is doomed!\n")


