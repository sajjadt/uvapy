# Doublets
from sys import stdin, stdout
from collections import deque
from string import ascii_lowercase

class Graph:
  def __init__(self, num_vertices, i_dic):
    self.num_vertices = num_vertices
    self.edges = [[] for i in range(self.num_vertices)]
    self.index_dictionary = i_dic
  def add_edge(self, u, v):
    self.edges[u].append(v)
    self.edges[v].append(u)

  def min_path(self, s, e):

    if s == e:
      return s

    distance_from_s = [-1] * self.num_vertices
    parent = [-1] * self.num_vertices
    
    def bfs(start, end):
      discovered = set([])

      q = deque([start])
      distance_from_s[start] = 0
      discovered.add(start)

      while len(q) > 0:
        v = q.popleft()
        
        for y in self.edges[v]:
      
          if not y in discovered:
            
            discovered.add(y)
            distance_from_s[y] = distance_from_s[v] + 1 
            parent[y] = v
            if y == end:
              return # Done

            q.append(y)
      
      return 

    bfs(s, e)
    p = e

    if distance_from_s[e] == -1:
      return []
    else:
      l = []
      while p != -1:
        l.append(self.index_dictionary[p])
        p = parent[p]
      return list(reversed(l))

dictionary = [{} for i in range(16+1)]
index_dictionary = []

# Process dictionary
word = stdin.readline().strip()
i = 0
while word != "":
  dictionary[len(word)][word] = i
  index_dictionary.append(word)
  word = input().strip()
  i += 1
  
# Create the graph
g = Graph(i, index_dictionary)
for i in range(1, 16+1):
  # Set edges between nodes with word len equal to i
  dic = list(dictionary[i].items())
  for j in range(0, len(dic)):
    word, word_i = dic[j]
    #change word
    for d in range(i):
      for ch in ascii_lowercase:
        if word[d] != ch:
          new_word = word[:d] + ch + word[d+1:]
          if new_word in dictionary[i]:
            g.add_edge(word_i, dictionary[i][new_word])


# Process queries
q = 1
line = stdin.readline().strip()
while line != "":
  s, t = line.split()
  sol = g.min_path(dictionary[len(s)][s], dictionary[len(t)][t])
  if q > 1:
    stdout.write("\n")
  if len(sol) == 0:
    stdout.write("No solution.\n")
  else:
    stdout.write("\n".join(sol)+"\n")
  line = stdin.readline().strip()
  q += 1
