num_tests = int(input())

for i in range(num_tests):
  sides = list(sorted(map(int, input().split())))
  if sides[0] == sides[1] == sides[2] == sides[3]:
    print("square")
  elif sides[0] == sides[1] and sides[2] == sides[3]:
    print("rectangle")
  else:
    perim = sum(sides)
    res = [perim - x for x in sides]
    is_banana = any(map(lambda x: x[0] >= x[1], zip(sides, res)))
    if is_banana:
      print("banana")
    else:
      print("quadrangle")