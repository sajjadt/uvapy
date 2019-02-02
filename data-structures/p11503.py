from time import time
from sys import stdin, stdout

# Dictionary based Disjoint Forest
class UFD:
  def __init__(self):
    self._id = {}
    self._count = {}
    self._rank = {}

  def find(self, p):
    id = self._id
    if not p in self._id:
      self._id[p] = p
      self._rank[p] = 0
      self._count[p] = 1
    else:
      while p != id[p]:
        id[p] = id[id[p]]   # Path compression using halving.
        p = id[p]     
    return p

  def connected(self, p, q):
    return self.find(p) == self.find(q)

  def union(self, p, q):
    id = self._id
    rank = self._rank
    count = self._count

    i = self.find(p)
    j = self.find(q)

    if i == j:
      return count[i]

    if rank[i] < rank[j]:
      id[i] = j
      count[j] += count[i]
      sum_count = count[j]
    elif rank[i] > rank[j]:
      id[j] = i
      count[i] += count[j]
      sum_count = count[i]
    else:
      id[j] = i
      rank[i] += 1
      count[i] += count[j]
      sum_count = count[i]
    
    return sum_count

s = time()
num_tests = int(stdin.readline().strip())

for t in range(num_tests):
  Q = int(stdin.readline().strip())
  
  uf = UFD()

  for q in range(Q):
    u, v = stdin.readline().strip().split()
    stdout.write("{}\n".format(uf.union(u, v)))
    
e = time()
# print(e - s)