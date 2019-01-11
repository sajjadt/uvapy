# from time import time
from collections import deque

# start = time()

while True:
  try:
    text = input()
    
    append_to_end = True
    container = deque()

    current_text = []
    for ch in text:
      if ch == "[":
        if append_to_end:
          container.append("".join(current_text))
        else:
          container.appendleft("".join(current_text))
          
        append_to_end = False
        current_text = []
      elif ch == "]":
        if append_to_end:
          container.append("".join(current_text))
        else:
          container.appendleft("".join(current_text))
           
        append_to_end = True
        current_text = []
      else:
        current_text.append(ch)

    if append_to_end:
      container.append("".join(current_text))
    else:
      container.appendleft("".join(current_text))
      
    print("".join(map(str, container)))

  except(EOFError):
    break

# end = time()
# print(end-start)