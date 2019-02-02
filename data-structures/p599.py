
num_cases = int(input())

# Graph is small (less than 27 nodes), and we can represent the disjoint set using an array. 

for c in range(num_cases):
  forest = [-1] * 26
  partition_id = 0
  while True:
    line = input().strip()
    if line[0] == "*":
      line = input().strip().split(",")
      # Report here
      num_acorns = len(line) - sum(x > 0 for x in forest)
      num_trees = len(set(forest)) - 1
      print("There are {} tree(s) and {} acorn(s).".format(num_trees, num_acorns))
      break
    else:
      u = ord(line[1]) - ord('A')
      v = ord(line[3]) - ord('A')
      if forest[u] == -1:
        if forest[v] == -1:
          partition_id += 1
          forest[u] = forest[v] = partition_id
        else:
          forest[u] = forest[v]
      else:
        if forest[v] == -1:
          forest[v] = forest[u]
        else:
          temp = forest[u]
          for i in range(len(forest)):
            if forest[i] == temp:
              forest[i] = forest[v]
    
