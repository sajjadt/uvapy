while True:
  try:
    num_sides = int(input())
    num_inputs = 1 << num_sides

    w = []
    total_w = []
    max_w = []

    N = [1 << i for i in range(num_sides)]
    
    for i in range(num_inputs):
      w.append(int(input()))

    for i in range(num_inputs):
      total = 0
      for n in N:
        total += w[i ^ n]
      total_w.append(total)

    for i in range(num_inputs):
      max_ = 0
      for n in N:
        if total_w[i] + total_w[i ^ n] > max_:
          max_ = total_w[i] + total_w[i ^ n]
      max_w.append(max_)
  
    print(max(max_w))
    
  except(EOFError):
    break