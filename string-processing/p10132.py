
def verify(f_d, sol, num_frags):
  count = 0
  for i in range(1, len(sol)):
    l = sol[:i]
    r = sol[i:]
    if not l in f_d and not r in f_d:
      continue
    if l in f_d and r in f_d:
      if f_d[l] != f_d[r]:
        return False
      count += (2*f_d[l] if l != r else f_d[l])
    else:
      return False
  return True if count == num_frags else False
    
from sys import stdin, stdout
cases = int(input())
for c in range(cases):
  
  if c == 0:
    stdin.readline()

  fragments = []
  f_d = {}
  line = input().strip()
  total_len = 0
  while line != "":
    fragments.append(line)
    total_len += len(line)

    if line in f_d:
      f_d[line] += 1
    else:
      f_d[line] = 1

    line = stdin.readline().strip()
    
  if len(fragments) == 2:
    stdout.write("".join(fragments[0] + fragments[1])+"\n")
  else:
    file_len = total_len*2 // len(fragments)
    i = 0
    checked = set()
    for j in range(1, len(fragments)):
      if len(fragments[i]) + len(fragments[j]) == file_len:
        if fragments[j] not in checked:
          if verify(f_d, fragments[i] + fragments[j], len(fragments)):
            stdout.write("".join(fragments[i] + fragments[j])+"\n")
            break
          if verify(f_d, fragments[j] + fragments[i], len(fragments)):
            stdout.write("".join(fragments[j] + fragments[i])+"\n")
            break
          checked.add(fragments[j])

  if c < cases - 1:
    stdout.write("\n")
  