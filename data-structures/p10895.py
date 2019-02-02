def transpose(mat, rows, cols):
  # Input matrix keeps the non-zero elements using an adjancy list in sorted order
  t_rows = cols
  ptr = [0] * rows
  t_mat = [[] for i in range(t_rows)]
  for i in range(t_rows):
    for j in range(rows):
      if ptr[j] < len(mat[j]) and mat[j][ptr[j]][0] == i+1:
        t_mat[i].append((j+1,  mat[j][ptr[j]][1]))
        ptr[j] += 1
  return t_mat


def print_mat(mat):
  for i in range(len(mat)):
    if len(mat[i]) == 0:
      print("0\n")
    else:
      ids = [str(p[0]) for p in mat[i]]
      vals = [str(p[1]) for p in mat[i]]
      print("{} {}".format(len(mat[i]), " ".join(ids)))
      print(" ".join(vals))


while True:
  try:
    rows, cols = list(map(int, input().split()))
    M = [[] for i in range(rows)]
    for i in range(rows):
      line = input().strip()
      if line == "0":
        input()
        continue
      else:
        ids = list(map(int, line.split()))
        num_vals = ids[0]
        vals = list(map(int, input().split()))
        for tup in zip(ids[1:], vals):
          M[i].append(tup)
        M[i].sort()

    T = transpose(M, rows, cols)
    print("{} {}".format(cols, rows))
    print_mat(T)
    
  except(EOFError):
    break