from os import linesep

test_no = 1
while True:
  rows, cols = list(map(int, input().split()))
  
  if rows == 0 and cols == 0:
    break
  
  if test_no > 1:
    print()

  field = []
  output_field = []
  for row in range(rows):
    field.append(list(input()))
    
  for i in range(rows):
    output_field.append([])
    for j in range(cols):
      if field[i][j] == '*':
        output_field[-1].append('*')
      else:
        num_bombs = 0
        
        if i > 0 and field[i-1][j] == '*': # prev row
          num_bombs += 1
        if i < rows - 1 and field[i+1][j] == '*': # next row
          num_bombs += 1
        if j > 0 and field[i][j-1] == '*': # prev col
          num_bombs += 1
        if j < cols - 1 and field[i][j+1] == '*': # next col
          num_bombs += 1

        if i > 0 and j > 0 and field[i-1][j-1] == '*': # prev row
          num_bombs += 1
        if i > 0 and j < cols - 1 and field[i-1][j+1] == '*': # next row
          num_bombs += 1
        if i < rows - 1 and j > 0 and field[i+1][j-1] == '*': # prev col
          num_bombs += 1
        if i < rows - 1 and j < cols - 1 and field[i+1][j+1] == '*': # next col
          num_bombs += 1


        output_field[-1].append(str(num_bombs))

  print("Field #" + str(test_no) + ":")
  print(linesep.join([str("".join(k)) for k in output_field]))

  test_no += 1

  
