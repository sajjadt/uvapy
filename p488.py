num_tests = int(input())

LIMIT = 1000
strs = [str(t)*t for t in range(LIMIT)]

for i in range(num_tests):
  input()
  amp = int(input())
  freq = int(input())

  for j in range(freq):
    for t in range(1, amp + 1):
      if t < LIMIT:
        print(strs[t])
      else:
        print(str(t)*t)
    for t in range(amp-1, 0, -1):
      if t < LIMIT:
        print(strs[t])
      else:
        print(str(t)*t)
    if not (i == num_tests - 1 and j == freq - 1):
      print()
