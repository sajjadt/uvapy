LINE_LEN = 25

while True:
  try:
    n = int(input())
    if n == 0:
      break
    surface = []
    max_len = 0

    for i in range(n):
      line = str(input())
      line = line.strip()
      l_space = line.find(' ')
      if l_space == -1:
        max_len = LINE_LEN
      else:
        r_space = line.rfind(' ')
        cur_len = l_space + LINE_LEN - r_space - 1
        if cur_len > max_len:
          max_len = cur_len
        
        surface.append(cur_len)
      

    res = sum(map(lambda x: max_len - x, surface))
    print(res)
  except(EOFError):
    break
