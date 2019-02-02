while True:
  n, d, r = list(map(int, input().split()))
  if n == 0:
    break
  
  routes1 = list(map(int, input().split()))
  routes2 = list(map(int, input().split()))

  # Best matching is to match the longest route with the shortest route
  routes1.sort(reverse=True)
  routes2.sort()
  
  print(sum(map(lambda x: r*(max((x[0] + x[1]) - d, 0)), zip(routes1, routes2))))