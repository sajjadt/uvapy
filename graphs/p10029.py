from sys import stdin, stdout
import sys
from functools import lru_cache
from sys import stdin, stdout
from time import time

sys.setrecursionlimit(10000)
class Graph:
  def __init__(self, words_dic):
    self.num_vertices = len(words_dic.items())
    self.edges = [set([]) for i in range(self.num_vertices)]

    def __set_data(words_dic):
      for w, i in words_dic.items():
        t = w
        for j in range(len(t)):
          t2 = t[:j] + t[j+1:] 
          # Removing/adding a letter
          if t2 in words_dic:
            if t < t2:
              self.edges[words_dic[t]].add(words_dic[t2])
            else:
              self.edges[words_dic[t2]].add(words_dic[t])
           
          # changing a letter
          for ch in range(ord(t[j]) + 1, ord('z') +1):
            t2 = t[:j] + chr(ch) +  (t[j+1:] if j < len(t) - 1 else "") 
            if t2 in words_dic:
              self.edges[i].add(words_dic[t2])
          
    __set_data(words_dic)

  def sol(self):
    # Works only on DAGs
    @lru_cache(maxsize=None)
    def max_dist(start):
      if len(self.edges[start]) == 0:
        return 1
      else:
        return 1 + max(max_dist(v) for v in self.edges[start])
    return max(max_dist(v) for v in range(self.num_vertices))

t1 = time()
words = []
while True:
  line = stdin.readline()
  if line == "":
    break
  word = line.strip()
  words.append(word)
  
words_dic = {w:i for i, w in enumerate(set(words))}
g = Graph(words_dic)

stdout.write("{}\n".format(g.sol()))
