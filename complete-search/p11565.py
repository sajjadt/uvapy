import time
from math import sqrt
from sys import stdout

num_tests = int(input())


cases = 0
start = time.time()
for t in range(num_tests):
  a, b, c = list(map(int, input().split()))

  # C0: xyz = b (positive) -> x and y and z > 0 and x < 0 and y < 0 and z > 0 since they will be sorted
  # conclude that z > 0

  # C1: -100 < x, y, z < 100
  # C2: abs value of one of numbers must be less than 23 -> xyz < 10000

  root3_b = int(pow(b, 0.3333)) + 2
  root_c = int(sqrt(c))
  found = False
  for z in range(-root3_b, root3_b):
    if found:
      break

    Z = z*z
    for y in range(-root_c, root_c + 1):
      if found:
        break

      if y == z:
        continue

      Y = y*y
      

      x = a - y - z

      if x == y or x ==z :
        continue
        
      if x > root_c:
        continue
      if x < -root_c:
        break
      
      if x * y * z != b:
        continue
      
      if x*x + y*y + z*z == c:
        stdout.write(" ".join(map(str, sorted([x, y, z]))) + "\n")
        found = True
    
  
  if not found:
    stdout.write("No solution.\n")

end = time.time()
# print(end - start)
