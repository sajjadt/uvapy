while True:
  dim = int(input())

  if dim == 0:
    break

  row_mismatch = -1
  col_mismatch = -1
  corrupt = False
  matrix = [[] for j in range(dim)]
  for i in range(dim):
    entry = list(map(int, input().split()))

    if corrupt:
      continue

    for j, e in enumerate(entry):
      matrix[j].append(e)
    if sum(entry) % 2:
      if row_mismatch == -1:
        row_mismatch = i + 1 
      else:
        corrupt = True
  
  if not corrupt:
    for j, entry in enumerate(matrix):
      if sum(entry) % 2:
        if col_mismatch == -1:
          col_mismatch = j + 1
        else:
          corrupt = True

  if not corrupt:
    if col_mismatch == row_mismatch == -1:
      print("OK")
    else:
      print("Change bit ({},{})".format(row_mismatch, col_mismatch))
  else:
    print("Corrupt")