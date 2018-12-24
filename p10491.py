
while True:
  try:
    num_cows, num_cars, num_show = list(map(int, input().split()))
    total = num_cars + num_cows 
  
    if num_show >= num_cows:
      p = 1
    else:
      p = (num_cars / total) * ( (num_cars - 1) / (total - 1 - num_show ) )
      p += (num_cows / total) * (num_cars / (total - 1 - num_show))
    
    print("{0:.5f}".format(p))
  except EOFError:
    break
