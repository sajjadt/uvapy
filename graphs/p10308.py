from collections import deque
from operator import itemgetter

def calculate_max_distance(graph):
  root = next(iter(graph.keys()))

  def __bfs(start):
    visited = set([])
    distance = {}
    distance[start] = 0
    q = deque([start])
    visited.add(start)
    while len(q) > 0:
      c = q.pop()
      for v in graph[c]:
        if not v[0] in visited:
          visited.add(v[0])
          distance[v[0]] = v[1] + distance[c]
          q.append(v[0])     
    return max(distance.items(), key=itemgetter(1))

  v, _ = __bfs(root)
  _, dist = __bfs(v)

  return dist

while True:
  try:
    line = input().strip()
    
    edges = {}
    while line != "":
      edge = list(map(int, line.split()))
      
      # Add the edge (destination, cost)
      if edge[0] in edges:
        edges[edge[0]].append((edge[1], edge[2]))
      else:
        edges[edge[0]] = [(edge[1], edge[2])]
        
      if edge[1] in edges:
        edges[edge[1]].append((edge[0], edge[2]))
      else:
        edges[edge[1]] = [(edge[0], edge[2])]
      
      line = input().strip()
      
    # Process the graph
    print(calculate_max_distance(edges))

  except(EOFError):
    # Last set of input
    print(calculate_max_distance(edges))
    break
