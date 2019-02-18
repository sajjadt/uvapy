
from functools import lru_cache

def num_of_paths(graph):
  
  @lru_cache(maxsize=None)
  def __num_of_paths(start):
    if len(graph[start]) == 0:
      return 1
    else:
      return sum(__num_of_paths(i) for i in graph[start])

  res = __num_of_paths(0)
  __num_of_paths.cache_clear()
  return res

def num_of_paths_dp(graph):
  # TODO
  # reverse the graph, start from the roots, modify the downstreams, revmoe the edges
  pass

case = 1
while True:
  try:
    if case > 1:
      input()
    
    n = int(input())
    
    graph = [[] for i in range(n)]
    r_graph = [[] for i in range(n)]

    for i in range(n):
      next_events = list(map(int, input().split()))
      graph[i] = next_events[1:]
    
    if case > 1:
      print()
    print(num_of_paths(graph))

    case += 1
  except(EOFError):
    break