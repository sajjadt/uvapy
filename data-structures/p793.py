from time import time
from sys import stdin, stdout
class UF:
  """An implementation of union find data structure.
  It uses weighted quick union by rank with path compression.
  """

  def __init__(self, N):
    """Initialize an empty union find object with N items.
    Args:
        N: Number of items in the union find object.
    """
    self._id = list(range(N))
    self._count = N
    self._rank = [0] * N

  def find(self, p):
    """Find the set identifier for the item p."""

    id = self._id
    while p != id[p]:
      id[p] = id[id[p]]   # Path compression using halving.
      p = id[p]     
    return p

  def connected(self, p, q):
    """Check if the items p and q are on the same set or not."""
    return self.find(p) == self.find(q)

  def union(self, p, q):
    """Combine sets containing p and q into a single set."""

    id = self._id
    rank = self._rank

    i = self.find(p)
    j = self.find(q)
    if i == j:
        return

    self._count -= 1
    if rank[i] < rank[j]:
        id[i] = j
    elif rank[i] > rank[j]:
        id[j] = i
    else:
        id[j] = i
        rank[i] += 1

s = time()
num_tests = int(input())
input()

for t in range(num_tests):
  N = int(input())
  
  uf = UF(N+1)
  num_connected = 0
  num_disconnected = 0
  
  queries = []

  line = stdin.readline().strip()
  while line != "":
    line = list(line.split())
    c = str(line[0])
    u = int(line[1])
    v = int(line[2])
    if c == "c":
      uf.union(u, v)
    else:
      queries.append(line)
      if uf.connected(u, v):
        num_connected += 1
      else:
        num_disconnected += 1
    try:
      line = stdin.readline().strip()
    except(EOFError):
      break

  if t > 0:
    stdout.write("\n")
  stdout.write("{},{}\n".format(num_connected, num_disconnected))
  
  
e = time()
# print(e - s)