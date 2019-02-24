from heapq import heappush, heappop
from math import ceil
from sys import stdin, stdout

class Edge:
  def __init__(self, u, v, cap):
    self.u = u
    self.v = v
    self.cap = cap

  # Functions needed by heapq functions
  def __lt__(self,other): 
    return self.cap > other.cap
  def __eq__(self,other): 
    return self.cap == other.cap
  def __str__(self): 
    return str("{}-{}:{}".format(self.u, self.v, self.cap))


def calc_max_cap(g, start, end):
  ''' Caclulate max cap from start to end via construction a maximum spanning tree '''
  
  cost = [0] * len(g)

  # Visit satrting node
  visited = set([start])
  q = []
  for edge in g[start]:
    heappush(q, edge)

  while len(q) > 0:
    cur = heappop(q)
    visited.add(cur.u)
    cost[cur.v] = max(min(cost[cur.u], cur.cap) if cost[cur.u] > 0 else cur.cap, cost[cur.v])

    for edge in g[cur.v]:
      if not edge.v in visited:
        heappush(q, edge)
  return (cost[end])

# Takes care of empty lines in the input
def _input():
  line = stdin.readline().strip()
  while line == "":
    line = stdin.readline().strip()
  return line

scenario = 1
while True:
  V, E = list(map(int, _input().split()))
  if V == E == 0:
    break
  
  g = [[] for i in range(V)]
  for i in range(E):
    u, v, cap = list(map(int, _input().split()))
    g[u-1].append(Edge(u-1, v-1, cap))
    g[v-1].append(Edge(v-1, u-1, cap))

  start, end, num_tourists = list(map(int, _input().split()))
  
  max_cap = calc_max_cap(g, start-1, end-1)
  sol = ceil(num_tourists / (max_cap-1))

  stdout.write("Scenario #{}\n".format(scenario))
  stdout.write("Minimum Number of Trips = {}\n\n".format(sol))

  scenario += 1