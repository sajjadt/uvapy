while True:
  n = int(input())

  if n == 0:
    break

  print("Printing order for {} pages:".format(n))
  r = n % 4

  sheet = 2
  # Printing the first sheet
  if r == 1:
    print("Sheet 1, front: Blank, 1")
    if n > 1: # at least 5
      print("Sheet 1, back : 2, Blank")  
      print("Sheet 2, front: Blank, 3")
      print("Sheet 2, back : 4, {}".format(n))
      n = n - 1 
      s = 5
      sheet += 1
    else:
      s = 2
  elif r == 2:
    print("Sheet 1, front: Blank, 1")
    print("Sheet 1, back : 2, Blank")
    s = 3
  elif r == 3:
    print("Sheet 1, front: Blank, 1")
    print("Sheet 1, back : 2, {}".format(n))
    n -= 1
    s = 3
  else:
    print("Sheet 1, front: {}, 1".format(n))
    print("Sheet 1, back : 2, {}".format(n-1))
    s = 3
    n -= 2

  # Printing the rest of the pages from [s...n]
  while s < n:
    print("Sheet {}, front: {}, {}".format(sheet, n, s))
    print("Sheet {}, back : {}, {}".format(sheet, s+1, n-1))

    s += 2
    n -= 2
    sheet += 1
