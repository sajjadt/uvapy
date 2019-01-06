num_tests = int(input())

for i in range(num_tests):
  line = input().split()
  a, b = line[0], line[1]

  c = str(int(a[::-1]) + int(b[::-1]))

  # remove trailing zeros
  c = c.rstrip("0")

  print(c[::-1])