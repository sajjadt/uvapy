while True:
  line = input().split()
  n, m = int(line[0]), int(line[1])

  if n == m == 0:
    break

  order = []
  in_edges = [(i, []) for i in range(n)]
  covered = []
  for i in range(m):
    line = input().split()
    e_from, e_to = int(line[0]) - 1, int(line[1]) - 1
    if not e_from in in_edges[e_to][1]:
      in_edges[e_to][1].append(e_from)

  while len(in_edges) > 0:
    target = -1
    for i in range(len(in_edges)):
      if len(in_edges[i][1]) == 0:
        target = i
        order.append(in_edges[i][0] + 1)
        break
      
    if target >= 0:
      v_id = in_edges[target][0]
      in_edges.remove(in_edges[target])
    
      for i in range(len(in_edges)):
        if v_id in in_edges[i][1]:
          in_edges[i][1].remove(v_id)
  
  print(" ".join(map(str, order)))