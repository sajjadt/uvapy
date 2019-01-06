
while True:
  num_items = int(input())
  if num_items == 0:
    break
  
  # Normal sort also works
  # items = list(sorted(map(int, input().split())))
  # print(" ".join(map(str, items)))

  buckets = [0 for i in range(101)]
  for age in map(int, input().split()):
    buckets[age] += 1
    
  for i, j in enumerate(buckets):
    if j > 0:
      if num_items > j:
        print(" ".join([str(i)]*j), end=" ")
      else: # last batch
        print(" ".join([str(i)]*j))
      num_items -= j
  
  
