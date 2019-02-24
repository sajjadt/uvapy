def pascal_triangle(num_rows):
  if num_rows == 1: return [[1]]

  triangle = [[1], [1, 1]] # pre-populate with the first two rows

  row = [1, 1] # Starts with the second row and calculate the next

  for i in range(2, num_rows):
    row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
    triangle.append(row)

  return triangle

table = pascal_triangle(50 + 1)

from sys import stdin, stdout

cases = int(stdin.readline().strip())
for c in range(cases):

  expression = stdin.readline().strip()
  s, k = expression.split("^")
  k = int(k)
  a, b = s[1:-1].split("+")
  
  out = []

  for i in range(len(table[k])):
    temp = ""
    if table[k][i] > 1:
      temp = str(table[k][i]) + "*"
    if i < k:
      temp += (a + "^"+ str(k-i)) if k > i + 1 else a
    if i > 0 and i < k:
      temp += "*"
    if i > 0:
      temp += (b + "^" + str(i)) if i > 1 else b 
    out.append(temp)
  
  stdout.write("Case {}: {}\n".format(c+1, "+".join(out)))