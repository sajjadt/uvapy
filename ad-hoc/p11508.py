from sys import stdin, stdout

while True:
  line = stdin.readline().strip()

  if line == "0":
    break
  
  line = list(map(int, line.split()))

  n = len(line)
  if any( x >= n or x < 0 for x in line):
    print("Message hacked by the Martians!!!")
  else:
    perm = [-1]*n

    unhandled = []
    for val in line:
      if perm[val] == -1:
        perm[val] = val
      else:
        unhandled.append(val)
        
    c_ptr = 0
    for val in unhandled:
      while perm[c_ptr] != -1:
        c_ptr += 1
      perm[c_ptr] = val

    stdout.write("{}\n".format(" ".join(map(str, perm))))