num_tests = int(input())

for t in range(num_tests):
  l = ""
  while l == "":
    l = input().strip()

  xl1, yl1, xr1, yr1 = list(map(int, l.split()))
  l = ""
  while l == "":
    l = input().strip()
  xl2, yl2, xr2, yr2 = list(map(int, l.split()))

  # print(xl1, yl1, xr1, yr1)
  if xl1 >= xr2 or xl2 >= xr1 or yl1 >= yr2 or yl2 >= yr1:
    print("No Overlap")
  else:
    print("{} {} {} {}".format(max(xl1, xl2), max(yl1, yl2), min(xr1, xr2), min(yr1, yr2)))
  if t < num_tests - 1:
    print()