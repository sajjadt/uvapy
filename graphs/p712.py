
from sys import stdin, stdout

var_id = {
  "x1": 0,
  "x2": 1,
  "x3": 2,
  "x4": 3,
  "x5": 4,
  "x6": 5,
  "x7": 6
}

case = 1
while True:
  
  d = int(stdin.readline().strip())

  if d == 0:
    break
  
  var = stdin.readline().split()
  leaves = list(stdin.readline().strip())

  num_queries = int(stdin.readline().strip())
  res = []
  for i in range(num_queries):
    query = list(map(int, stdin.readline().strip()))

    index = 0
    for k in var:
      index = index*2 +  query[var_id[k]]

    res.append(leaves[index])

  stdout.write("S-Tree #{}:\n{}\n\n".format(case, "".join(res)))
  case += 1