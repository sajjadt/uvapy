from math import atan2

# O(n*logn) solution

while True:
  n = input().strip() 
  while n == "":
    n = input().strip() 

  n = int(n)
  if n == 0:
    break

  points = []
  for i in range(n):
    ax, ay, bx, by = list(map(int, input().split()))
    points.append([ax, ay, i])
    points.append([bx, by, i])

  cx, cy = list(map(int, input().split()))
  # Sort points based on degree
  points.sort(key=lambda p: atan2(p[1]-cy, p[0]-cx))
  seen = set()

  max_hits = 0
  hits = 0
  for p in points:
    if not p[2] in seen:
      hits += 1
      seen.add(p[2])
      if hits > max_hits:
        max_hits = hits
    else:
      hits -= 1
      seen.remove(p[2])
  
  print(max_hits)
