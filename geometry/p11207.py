while True:
  n = int(input())
  if n == 0:
    break
  
  best_v = best_i = 0
  for i in range(n):
    h, w = list(map(int, input().split()))
    
    if w < h:
      w, h = h, w
    # Now we can assume w > h

    # Two options to cut the paper into four squares
    # 1:
    #  ______
    # |  |  | 
    # |--|--|
    # |__|__|
    case_1 = min(h, w) / 2
    # 2:
    #  ____________
    # |__|__|__|__|
    case_2 = min(h, w/4)
    if max(case_1, case_2) > best_v:
      best_i = i + 1
      best_v = max(case_1, case_2)
  print(best_i)