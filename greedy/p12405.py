num_tests = int(input())

for i in range(num_tests):
  x = int(input())
  field = str(input())

  num_scarcrows = 0
  place_on_next = False
  last_scracrow = -2
  for j, ch in enumerate(field):
    if ch == ".":
      if j - last_scracrow > 1:
        last_scracrow = j + 1
        num_scarcrows += 1
  
  print("Case {}: {}".format(i + 1, num_scarcrows))