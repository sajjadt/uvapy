from math import sqrt
from sys import stdin, stdout

def simulate(n):
  balls = [0] * n
  i = 1
  can_place_more = True
  while can_place_more:
    can_place_more = False
    for j in range(n):
      if balls[j] == 0:
        balls[j] = i 
        i += 1
        can_place_more = True
        break
      else:
        sum_val = balls[j] + i
        root = sqrt(sum_val)
        if int(root + 0.5) ** 2 == sum_val:
          balls[j] = i
          i += 1
          can_place_more = True
          break
  return i - 1

pre_calc_res = [
  0, 1, 3, 7, 11, 17, 23, 31, 39, 49, 59, 71, 83, 97, 111, 127, 143,
  161, 179, 199, 219, 241, 263, 287, 311, 337, 363, 391, 419,
  449, 479, 511, 543, 577, 611, 647, 683, 721, 759, 799, 839, 881, 923, 967, 1011, 1057, 1103, 1151, 1199, 1249, 1299,
]

cases = int(stdin.readline().strip())

for c in range(cases):
  n = int(stdin.readline().strip())
  stdout.write("{}\n".format(pre_calc_res[n]))