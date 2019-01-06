num_tests = int(input())

for test in range(num_tests):
  s, d = list(map(int, input().split()))

  if (s+d) % 2:
    print("impossible")
    continue

  a = (s + d)//2
  b = s - a

  if a < b:
    b, a = a, b

  if a >= 0 and b >= 0:
    print("{} {}".format(a, b))
  else:
    print("impossible")   