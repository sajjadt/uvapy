from collections import deque

def reachable(graph, start_v):
  seen = set() 
  working_set = deque([start_v])
  
  while len(working_set) > 0:
    v = working_set.pop()
    for e in graph[v]:
      if not e in seen:
        seen.add(e)
        working_set.append(e)
  
  return seen


while True:
  n = int(input())

  if n == 0:
    break
  
  graph = [[] for i in range(n)]
  all_vertices = set([i for i in range(n)])

  # Read Graph
  while True:
    line = input() 
    if line == "0":
      break
    
    edges = list(map(int, line.split()))
    start_node = edges[0] - 1
    for e in edges[1:-1]:
      graph[start_node].append(e-1)
  
  # Read Queries
  queries = list(map(int, input().split()))
  for query in queries[1:]:
    non_reachables = all_vertices - reachable(graph, query-1)
    out_len = len(non_reachables)
    if out_len > 0:
      non_reachables = sorted(list(non_reachables))
      print("{} {}".format(out_len, " ".join(map(lambda x: str(x+1), non_reachables))))
    else:
      print("0")

