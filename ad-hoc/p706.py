# 7 Edges: top to botton and left to right
#   __
#  |  |
#   __
#  |  |
#   --

digits = {
  "0": [0, 1, 2, 4, 5, 6],
  "1": [2, 5],
  "2": [0, 2, 3, 4, 6],
  "3": [0, 2, 3, 5, 6],
  "4": [1, 2, 3, 5],
  "5": [0, 1, 3, 5, 6],
  "6": [0, 1, 3, 4, 5, 6],
  "7": [0, 2, 5],
  "8": [0, 1, 2, 3, 4, 5, 6],
  "9": [0, 1, 2, 3, 5, 6],
}

def draw_digit(board, index, value, width):
  start_col = index*(width+2) + index
  for edge in digits[value]:
    if edge == 0:
      board[0][start_col+1:start_col+1+width] = ['-']*width
    elif edge == 1:
      for i in range(1, w+1):
        board[i][start_col] = "|"
    elif edge == 2:
      for i in range(1, w+1):
        board[i][start_col+1+w] = "|"
    elif edge == 3:
      board[w+1][start_col+1:start_col+1+width] = ['-']*width
    elif edge == 4:
      for i in range(1, w+1):
        board[i + w + 1][start_col] = "|"
    elif edge == 5:
      for i in range(1, w+1):
        board[i + w + 1][start_col+1+w] = "|"
    elif edge == 6:
      board[2*w+2][start_col+1:start_col+1+width] = ['-']*width
    

from sys import stdin, stdout
while True:
  w, num = stdin.readline().strip().split()
  if w == "0":
    break

  w = int(w)

  word_len = len(num) * (w+2) + len(num) - 1
  board = [[" "]*(word_len) for i in range(2*w+3) ]

  for i,digit in enumerate(num):
    draw_digit(board, i, digit, w)
  
  stdout.write("\n".join(["".join(b) for b in board]) + "\n\n")
