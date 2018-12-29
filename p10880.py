from math import sqrt
# import time
# start = time.time()

num_tests = int(input())

for test in range(num_tests):
  c, r = list(map(int, input().split()))
  diff = c - r

  if diff == 0:
    print("Case #{}: 0".format(test+1))
  else:
    root = int(sqrt(diff))

    sol = set()
    for i in range(1, root+1):
      if diff % i == 0:
        
        if i > r:
          sol.add(i)
        
        q = diff // i
        if q > r:
          sol.add(q)
          
    items = len(sol)
    sol_l = sorted(list(sol))

    # sol_l = []
    # sol_h = []
    # items = 0
    # for i in range(1, root+1):
    #   if diff % i == 0:
        
    #     if i > r:
    #       sol_l.append(i)
    #       items += 1
        
    #     q = diff // i
    #     if q > r:
    #       sol_h.append(q)
    #       items += 1
    # sol_l += reversed(sol_h)

    if items == 0:
      print("Case #{}:".format(test+1))
    else:
      print("Case #{}: {}".format(test+1, " ".join(map(str, sol_l))))

# end = time.time()
# print("Took {} seconds".format(end - start))