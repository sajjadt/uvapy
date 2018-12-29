while True:
  try:
    ch_from, ch_to = list(map(int, input().split()))
    
    if ch_from == ch_to == -1:
      break
    
    # either go up or down
    distance_up = ch_to - ch_from
    if distance_up < 0:
      distance_up += 100
    distance_down = ch_from - ch_to
    if distance_down < 0:
      distance_down += 100
    
    print(min(distance_down, distance_up))
  except EOFError:
    break
  