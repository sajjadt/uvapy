from math import sqrt, floor

buffer = []
def get_next_int():
  ''' Returns a list contains next n integers read from the console '''
  global buffer

  while len(buffer) < 1:
    inp = stdin.readline()
    if inp == "" :
      return -1
    else:
      inp = inp.strip()
      buffer += list(map(int, inp.split()))
      
  ret = buffer[0]
  buffer = buffer[1:]
  
  return ret


def cantor_term(index):
  # sum[1, 2, 3, 4, ..., n] = n * (n+1) // 2
  r = floor(sqrt(2*index))
  if r*(r+1) >= 2*index:
    r -= 1
  diff = index - r*(r+1)//2 - 1
  m, n = diff + 1, r+1-diff
  return (m, n) if r % 2 == 1 else (n, m)

from sys import stdin, stdout
while True:
  index = get_next_int()
  if index == -1:
    break
  stdout.write("TERM {} IS {}/{}\n".format(index, *cantor_term(index)))