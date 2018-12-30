from math import ceil

test_no = 1
while True:
  r, n = list(map(int, input().split()))
  
  if r == n == 0:
    break

  if n >= r:
    print("Case {}: 0".format(test_no))
  else:
    sol = int(ceil((r - n) / n))
    if sol <= 26:
      print("Case {}: {}".format(test_no, sol))
    else:
      print("Case {}: impossible".format(test_no))

  test_no += 1