
#!/usr/bin/python3
from math import log, ceil

while True:
  try:
    line = input()

    # find consecutive blocks of space
    num_spaces = 0
    max_spaces = 0 
    for ch in line:
      if ch == ' ':
        num_spaces += 1
        if num_spaces > max_spaces:
          max_spaces = num_spaces
      else :
        num_spaces = 0 
    
    print(ceil(log(max_spaces, 2)) if max_spaces > 0 else 0)
  except EOFError:
    break

