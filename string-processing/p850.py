from sys import stdin, stdout
from string import ascii_lowercase

num_cases = int(stdin.readline().strip())
stdin.readline()

pattern = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
pattern_l = [len(x) for x in pattern]
pattern_unique_chars = set(list("".join(pattern)))

for c in range(num_cases):
  t = []
  lines = []
  line = stdin.readline().strip()
  while line != "":
    lines.append(line)
    line = stdin.readline().strip()

  has_sol = False
  # find one occurance of pattern
  for line in lines:
    l = [len(x) for x in line.split()]
    if l == pattern_l:  # check for pattern
      t = line.split()
      if not t[0] == t[6]:  # match 'the'
        continue
    
      if not t[2][2] == t[3][1] == t[5][0] == t[8][1]:  # match ' o'
        continue

      if not t[0][2] == t[5][2]:  # match 'e'
        continue

      if not t[2][1] == t[5][3]: # match 'r'
        continue

      if not len(pattern_unique_chars) == len(set(list("".join(t[:len(pattern)])))):
        continue

      has_sol = True
      break
      
  if c > 0:
    stdout.write("\n")

  if not has_sol:
    stdout.write("No solution.\n")
    continue
  

  m1 = list("".join(t))
  m2 = list("".join(pattern))

  mapping = {}
  for p in zip(m1, m2):
    mapping[p[0]] = p[1]
  mapping[" "] = " "

  for line in lines:
    stdout.write("{}\n".format("".join([mapping[x] for x in line])))
