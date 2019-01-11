num_tests = int(input())

total_allowed = 0
max_dim = [56, 45, 25, 7]
for t in range(num_tests):
  dim = list(map(float, input().split()))

  # Check dimension
  if any([x[0] > x[1] for x in zip(dim, max_dim)]):
    if sum(dim[0:3]) > 125:
      print("0")
      continue  

  if dim[3] > 7:
    print("0")
    continue

  print("1")
  total_allowed += 1
print(total_allowed)
  

