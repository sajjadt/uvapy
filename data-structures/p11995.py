from sys import stdin, stdout
from collections import deque
from heapq import *

while True:
  try:
    n = int(input()) 

    n_stack = []  # stack
    n_queue = deque()
    n_heap = []

    is_stack = is_queue = is_heap = True
    num_elements = 0
    for i in range(n):
      query = list(map(int, stdin.readline().strip().split()))
      if query[0] == 1:
        if is_stack:
          n_stack.append(query[1])
        if is_queue:
          n_queue.appendleft(query[1])
        if is_heap:
          heappush(n_heap, -query[1])
        num_elements += 1
      elif query[0] == 2:
        if num_elements == 0:
          is_heap = is_queue = is_stack = False
        else:
          if is_heap and heappop(n_heap) != -query[1]:
            is_heap = False
          if is_queue and n_queue.pop() != query[1]:
            is_queue = False
          if is_stack and n_stack.pop() != query[1]:
            is_stack = False
        num_elements -= 1
      
    if not is_stack and not is_heap and not is_queue:
      print("impossible")
    elif is_stack and not is_heap and not is_queue:
      print("stack")
    elif is_heap and not is_stack and not is_queue:
      print("priority queue")
    elif is_queue and not is_stack and not is_heap:
      print("queue")
    else:
      print("not sure")

  except(EOFError):
    break