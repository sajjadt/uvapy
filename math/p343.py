
from sys import stdin, stdout

def find_min_base(num):
  min_base = 2
  for ch in num:
    if ch.isdigit():
      base = int(ch) + 1
    else:
      base = ord(ch) - ord('A') + 11
    min_base = max(base, min_base)
  return min_base

while True:
  line = stdin.readline()
  if line == "":
    break

  n, m = line.strip().split()
  
  if len(n) > 1:
    n = n.lstrip("0")
  if len(m) > 1:
    m = m.lstrip("0")

  base_start_n = find_min_base(n)
  base_start_m = find_min_base(m)

  # Brute force
  # match = False
  # for i in range(base_start_n, 37):
  #   if match:
  #     break
  #   for j in range(base_start_m, 37):
  #     if int(n, i) == int(m, j):
  #       match = True
  #       print("{} (base {}) = {} (base {})".format(n, i, m, j))
  #       break
  # if not match:
  #   print("{} is not equal to {} in any base 2..36".format(n, m))

  # A bit more clever than brute force
  i = base_start_n
  j = base_start_m
  match = False

  while not match and i < 37 and j < 37:
    n_val = int(n, i)
    m_val = int(m, j)
    if n_val == m_val:
      match = True
    elif n_val > m_val:
      j += 1
    else:
      i += 1

  if match:
    stdout.write("{} (base {}) = {} (base {})\n".format(n, i, m, j))
  else:
    stdout.write("{} is not equal to {} in any base 2..36\n".format(n, m))

  