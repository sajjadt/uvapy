from sys import stdin, stdout

num = int(stdin.readline().strip())

for i in range(num):
  text = str(stdin.readline().strip())

  indices = [0] * (len(text) + 1)
  for j, t in enumerate(text):
    if t == "R":
      indices[j+1] = indices[j] + 1
    elif t == "C":
      indices[j+1] = indices[j]
    elif t == "F":
      indices[j+1] = indices[j] - 1
    else:
      raise ValueError("Unexpected character {t} at index {}.".format(t, j))

  min_v = min(indices)
  max_v = max(indices)
  
  # 2D array allocaiton
  chart = [["|"," "] + [" "]*len(text) for j in range(max_v - min_v + 2) ]
  chart[0] = ["-"]* (len(text) + 3)
  chart[0][0] = "+"
  # Normalize
  indices = list(map(lambda x: x - min_v , indices))
  ch_indices = []
  for j in range(len(indices)):
    if j > 0:
      disp = indices[j] - indices[j-1]
      if disp == 0:
        ch_indices.append("_")
      elif disp == 1:
        ch_indices.append("/")
      else:
        ch_indices.append("\\")
      
  
  for j, pair in enumerate(zip(indices[0:-1], ch_indices)):
    if pair[1] == "\\":
      chart[pair[0]-1+1][j+2] = pair[1] 
    else:
      chart[pair[0]+1][j+2] = pair[1] 

  stdout.write("Case #{}:\n".format(i+1))
  # chart = map(lambda x: "".join(x).rstrip(), chart)
  lines = ["".join(x).rstrip() for x in reversed(chart)]
  if len(lines[0]) > 1:
    stdout.write("\n".join(lines))
    stdout.write("\n")
  else:
    stdout.write("\n".join(lines[1:]))
    stdout.write("\n")
  print()
