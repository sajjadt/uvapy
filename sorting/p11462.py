while True:
  num_items = int(input())
  if num_items == 0:
    break
  items = list(sorted(map(int, input().split())))
  
  print(" ".join(map(str, items)))