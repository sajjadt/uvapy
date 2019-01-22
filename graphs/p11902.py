import sys
from types import MethodType
from sys import stdin, stdout
from collections import deque

# import Graph  from lib/graph here...
sys.path.insert(0, './lib/')
from graph import Graph

num_cases = int(input())

for t in range(num_cases):
  v = int(input())
  g = Graph(v)
  for i in range(v):
    adj_list = list(map(int, input().split()))
    g.edges[i] = [i for i,v in enumerate(adj_list) if v == 1]
  
  g.dfs(0)
  stdout.write("Case {}:\n".format(t+1))
  stdout.write("+" + "-"*(2*v-1) + "+\n" )


  seen0 = [False] * v
  def process_vertex_0(v):
    seen0[v] = True
  g.process_vertex = process_vertex_0
  g.bfs(0)
  ret_str = ["Y" if i else "N" for i in seen0]
  stdout.write("|" + "|".join(ret_str) + "|\n" )
  stdout.write("+" + "-"*(2*v-1) + "+\n" )

  for i in range(1, v):
    seen = [False] * v

    def valid_edge(start, end):
      return False if start == i or end == i else True
    def process_vertex(v):
      seen[v] = True

    g.valid_edge = valid_edge
    g.process_vertex = process_vertex
    g.bfs(0)
    pseen = map(lambda p: p[0] ^ p[1], zip(seen0, seen))
    
    ret_str = ["Y" if i else "N" for i in pseen]
    stdout.write("|" + "|".join(ret_str) + "|\n" )
    stdout.write("+" + "-"*(2*v-1) + "+\n" )