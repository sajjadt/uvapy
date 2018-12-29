def pairwise(iterable):
  it = iter(iterable)
  a = next(it, None)

  for b in it:
    yield (a, b)
    a = b

num_tests = int(input())

for test in range(num_tests):
  num_walls = int(input())
  walls = list(map(int, input().split()))

  h = l = 0
  if len(walls) >= 2:
    for c, n in pairwise(walls):
      if n > c:
        h += 1
      elif n < c:
        l += 1
  
  print("Case {}: {} {}".format(test + 1, h, l))