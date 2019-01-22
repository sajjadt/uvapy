import sys
from sys import stdin, stdout

# Simple graph traversal framework
class Graph:
  def __init__(self, num_vertices):
    self.edges = [[] for i in range(num_vertices)]
    # Early termination flag for DFS
    self.finished = False 
    self.num_vertices = num_vertices
    
    self.processed = [False] * num_vertices
    self.discovered = [False] * num_vertices

    self.parent = [-1] * self.num_vertices

  def __set_data(self, matrix):
    for i, row in enumerate(matrix):
      for j, e in enumerate(row):
        if e == 1: # TODO: weighted graph
          self.edges[i].append(j)

  @staticmethod
  def from_matrix(adj_matrix):
    g = Graph(len(adj_matrix))
    g.__set_data(adj_matrix)
    return g

  def dfs(self, start):
    
    self.processed = [False] * self.num_vertices
    self.discovered = [False] * self.num_vertices

    # self.parent = [-1] * self.num_vertices
    self.__dfs(start)
    

  def __dfs(self, v):
    self.discovered[v] = True
    self.process_vertex(v)

    for y in self.edges[v]:
      if self.valid_edge(v, y):
        if not self.discovered[y]:
          # self.parent[y] = v
          self.__dfs(y)
        
    self.processed[v] = True

  def process_vertex(self, v):
    pass  

  def process_edge(self, v_start, v_end):
    pass

  def valid_edge(self, v_start, v_end):
    return True 


def num_connected_components(g):
  # Find articulation points
  vertices = set([i for i in range(g.num_vertices)])
  def process_vertex(v):
    if v in vertices:
      vertices.remove(v)
  
  g.process_vertex = process_vertex
  num_connected_components = 0

  while len(vertices) > 0:
    g.dfs(vertices.pop())
    num_connected_components += 1
  
  return num_connected_components 

while True:
  v = int(stdin.readline().strip())
  if v == 0:
    break

  adj_matrix = [ [0]*v for i in range(v) ]
  while True:
    inp = stdin.readline().strip()
    if inp == "0":
      break

    edges = list(map(lambda x: int(x)-1, inp.split()))

    v_start = edges[0]
    for v in edges[1:]:
      adj_matrix[v_start][v] = 1
      adj_matrix[v][v_start] = 1

  g = Graph.from_matrix(adj_matrix)
  num_c = num_connected_components(g)
  res = 0
  for v in range(g.num_vertices):
    # Disconnect v
    valid_edge = lambda start, end: False if start == v or end == v else True 
    g.valid_edge = valid_edge
    num_temp = num_connected_components(g) - 1 # since it also counts the removed vertex
    if num_temp > num_c:
      res += 1
    # Reconnect v (happens automatically)
  
  print(res)