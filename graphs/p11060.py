
# in_edges = [(vertex id, [vertex input edges])]
def topological_sort(in_edges):
  order = []
  while len(in_edges) > 0:
    target = -1
    for i in range(len(in_edges)):
      if len(in_edges[i][1]) == 0:
        target = i
        order.append(in_edges[i][0])
        break
      
    if target >= 0:
      v_id = in_edges[target][0]
      in_edges.remove(in_edges[target])
    
      for i in range(len(in_edges)):
        if v_id in in_edges[i][1]:
          in_edges[i][1].remove(v_id)
  return order


test_no = 1
while True:
  try:
    n = int(input())
    
    g = {}
    for i in range(n):
      g[str(input())] = []
    
    e = int(input())
    for i in range(e):
      f, t = list(map(str, input().split()))
      if f not in g[t]:
        g[t].append(f)
    
    g_list = [(k, v) for k, v in g.items()]
    
    order = topological_sort(g_list)
    
    order = " ".join(order)
    print ("Case #{}: Dilbert should drink beverages in this order: {}.".format(test_no, order))
    print()
    input()
    test_no += 1

  except(EOFError):
    break

