from sys import stdin, stdout
cases = int(stdin.readline().strip())

for c in range(cases):
  line = str(stdin.readline().strip().strip())

  found = False
  dance_len = 1
  while not found:    
    next_rep = line.find(line[:dance_len], dance_len)
    
    if next_rep == -1: # Not found
      break

    dance = line[0: next_rep]
    dance_len = len(dance)

    found = True
    i = 0
    for j in range(next_rep, len(line)):
      if line[j] != dance[i]:
        found = False 
        break
      i = (i+1) % len(dance)
    
    dance_len += 1
    

  rem = len(line) % len(dance)
  res = ""
  i = 0
  while i < 8:
    res += dance[rem % len(dance)]
    i += 1 
    rem += 1
  res += "..."
  stdout.write("{}\n".format(res))

