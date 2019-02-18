from collections import deque

buffer = []
def get_next_int(n):
  ''' Returns a list contains next n integers read from the console '''
  global buffer

  while len(buffer) < n:
    inp = input()
    if inp == "" :
      continue
    else:
      buffer += list(map(int, inp.split()))
      
  ret =  buffer[0:n]
  buffer = buffer[n:]
  
  return ret

in_edges = {}
edges = {}
vertices = set([])
num_edges = 0
case = 1
has_loop = False
while True:
  u, v = get_next_int(2)
  if u < 0:
    break

  if u == v == 0:
    # process
    
    if len(vertices) == 0:
      res = "a tree"
    elif has_loop or len(vertices) != num_edges + 1:
      res = "not a tree"
    else:
      degree_of_zero = 0
      root = -1
      for v in vertices:
        if not v in in_edges:
          degree_of_zero += 1
          root = v

      if degree_of_zero != 1:
        res = "no a tree"
      else:
        #TODO Check reachablity f
        reached = set()
        reached.add(root)
        q = deque([root])
        while len(q) > 0:
          c = q.pop()
          if c in edges:
            for edge in edges[c]:
              if not edge in reached:
                reached.add(edge)
                q.append(edge)

        if len(reached) == len(vertices):  
          res = "a tree"
        else:
          res = "not a tree"
    print("Case {} is {}.".format(case, res))

    # make a new graph
    vertices.clear()
    in_edges.clear()
    edges.clear()
    num_edges = 0
    case += 1
    has_loop = False
  else:
    # add to current graph
    

    vertices.add(u)
    vertices.add(v)

    if u == v:
      has_loop = True
      continue

    num_edges += 1
    if not v in in_edges:
      in_edges[v] = 1
    else:
      in_edges[v] += 1

    if not u in edges:
      edges[u] = [v]
    else:
      edges[u].append(v)
