from itertools import combinations
# import time
from sys import stdout

def comb_n_6_gen(elements):
  if len (elements) < 6:
    yield None
  
  le = elements
  for i0 in range(0, len(elements)-5):
    for i1 in range(i0+1, len(elements)-4):
      for i2 in range(i1+1, len(elements)-3):
        for i3 in range(i2+1, len(elements)-2):
          for i4 in range(i3+1, len(elements)-1):
            for i5 in range(i4+1, len(elements)):
              yield([le[i0], le[i1], le[i2], le[i3], le[i4], le[i5]])

# start = time.time()
test_no = 0
while True:
  line = input().strip()
  if line[0] == "0":
    break

  if test_no > 0:
    stdout.write("\n")

  line = list(map(int, line.split()))

  stdout.write(
    "\n".join([
      " ".join(map(str, p)) for p in combinations(line[1:], 6)
      # " ".join(map(str, p)) for p in comb_n_6_gen(line[1:])
      ])
    + "\n")
  
  test_no += 1

# end = time.time()
# print(end - start)