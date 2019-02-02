num_cases = int(input())

def traverse_graph():
  ''' Using BFS calculate distance of each valid input from the solution'''
  ''' Store the result in a dictionary input -> path '''

  from collections import deque
  nodes = {}

  working_q = deque(["12345678x"])
  nodes["12345678x"] = ""

  while len(working_q) > 0:
    curr = working_q.popleft()
    
    hole_loc = curr.index("x")
    row, col = divmod(hole_loc, 3)

    # Down
    if row < 2:      
      new_board = list(curr)
      new_loc = hole_loc + 3
      new_board[hole_loc], new_board[new_loc] = new_board[new_loc], new_board[hole_loc]
      new_board = "".join(new_board)
      if not new_board in nodes:
        working_q.append(new_board)
        nodes[new_board] = "u" + nodes[curr]
    # Up
    if row > 0:
      new_board = list(curr)
      new_loc = hole_loc - 3
      new_board[hole_loc], new_board[new_loc] = new_board[new_loc], new_board[hole_loc]
      new_board = "".join(new_board)
      if not new_board in nodes:
        working_q.append(new_board)
        nodes[new_board] = "d" + nodes[curr]
    # Right
    if col < 2:
      new_board = list(curr)
      new_loc = hole_loc + 1
      new_board[hole_loc], new_board[new_loc] = new_board[new_loc], new_board[hole_loc]
      new_board = "".join(new_board)
      if not new_board in nodes:
        working_q.append(new_board)
        nodes[new_board] = "l" + nodes[curr]
    # Left
    if col > 0:
      new_board = list(curr)
      new_loc = hole_loc - 1
      new_board[hole_loc], new_board[new_loc] = new_board[new_loc], new_board[hole_loc]
      new_board = "".join(new_board)
      if not new_board in nodes:
        working_q.append(new_board)
        nodes[new_board] = "r" + nodes[curr]

  nodes["12345678x"] = "uudd"
  return nodes

from time import time

sol = traverse_graph()

for t in range(num_cases):
  input()
  board = "".join(input().split())
  if t > 0:
    print()
  if board in sol:
    print(sol[board])
  else:
    print("unsolvable")