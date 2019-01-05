import itertools
from collections import deque

num_tests = int(input())

class Node():
  def __init__(self, id):
    self.id = id
    self.to = []
    self.distance = -1
  def add(self, n):
    if not n in self.to:
      self.to.append(n)

for i in range(num_tests):
  line = input().split()
  np, na = int(line[0]), int(line[1])
  g = {}

  for p in range(np):
    paper = input().strip()
    p_authors, title = paper.split(":")
    p_authors = p_authors.split(", ")
    p_authors = [p_authors[i] +"," + p_authors[i+1] for i in range(0, len(p_authors) - 1, 2)]
    
    for u, v in itertools.combinations(p_authors, 2):
      if not u in g:
        g[u] = Node(u)
      if not v in g:
        g[v] = Node(v)
      
      g[v].add(g[u])
      g[u].add(g[v])

  erdos = "Erdos,P."
  if erdos in g:
    root = g[erdos]
    root.distance = 0

    visited = deque([root])
    while len(visited) > 0:
      v = visited.popleft()
      for n in v.to:
        if n.distance == -1 or n.distance > v.distance + 1:
          n.distance = v.distance + 1
          visited.append(n)
        
  print("Scenario {}".format(i+1))
  for a in range(na):
    author = input()
    author_s = author.replace(' ', '')
    distance = "infinity" if not author_s in g else str(g[author_s].distance) if g[author_s].distance > -1 else "infinity"   
    print("{} {}".format(author, distance))