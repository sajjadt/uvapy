num_tests = int(input())

for i in range(num_tests):
  num_rects = int(input())

  line = list(map(int, input().split()))
  # Represent rectangle with a list of two tuples (x_ll, y_ll), (x_ur, y_ur)
  common_rect = [(line[0], line[1]), (line[2], line[3])]

  no_overlap = False
  for j in range(1, num_rects):
    line = list(map(int, input().split()))

    # Just read the input if there is no overlap between previous rectangles
    if no_overlap:
      continue

    new_rect = [(line[0], line[1]), (line[2], line[3])]

    xl = max(new_rect[0][0], common_rect[0][0])
    xr = min(new_rect[1][0], common_rect[1][0])

    yl = max(new_rect[0][1], common_rect[0][1])
    yr = min(new_rect[1][1], common_rect[1][1])

    if xr > xl and yr > yl:
      common_rect = [(xl, yl), (xr, yr)]
    else:
      no_overlap = True
  
  area = 0 if no_overlap else (common_rect[1][0] - common_rect[0][0]) * (common_rect[1][1] - common_rect[0][1])

  print("Case {}: {}".format(i+1, area))