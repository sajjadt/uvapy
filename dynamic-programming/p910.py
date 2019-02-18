from functools import lru_cache

def num_paths(graph, m):

  if not "A" in graph:
    return 0

  @lru_cache(maxsize=32*32)
  def _num_paths(start, m):

    if m == 0:
      return 1 if graph[start][2] else 0
    
    ret = _num_paths(g[start][0], m-1)
    ret += _num_paths(g[start][1], m-1)
    
    return ret
  
  ret = _num_paths("A", m)
  _num_paths.cache_clear()
  return ret


def _input():
  line = input().strip()
  while line == "":
    line = input().strip()
  return line

while True:
  try:
    n_e = int(_input())
    g = {}
    for i in range(n_e):
      edge = _input().split()
      g[edge[0]] = (edge[1], edge[2], True if edge[3] == "x" else False)
    m = int(_input())
    print(num_paths(g, m))
  except(EOFError):
    break