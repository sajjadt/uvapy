num_tests = int(input())

for i in range(num_tests):
  input()

  v, e = list(map(int, input().split()))
  values = list(map(int, input().split()))
  edges = [[] for i in range(v)]
  for j in range(e):
    f, t = list(map(int, input().split()))
    edges[f].append(t)
  
  root = 0
  total = 0
  while len(edges[root]) > 0:
    t = [(x, values[x]) for x in edges[root]]
    dst = max(t, key=lambda x:x[1])
    total += dst[1]
    root = dst[0]
  
  print("Case {}: {} {}".format(i+1, total, root))

  