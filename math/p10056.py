

num_tests = int(input())
for test in range(num_tests):
  x = input().split()
  num_players = int(x[0])
  p = float(x[1])
  player = int(x[2])
  q = 1 - p
  if p == 1:
    solution = 1 if player == 1 else 0
  elif p == 0:
    solution = 0
  else:
    solution = p * pow(q, player-1) * ( 1 / (1 - pow(q, num_players)))
  print("{0:.4f}".format(solution))
