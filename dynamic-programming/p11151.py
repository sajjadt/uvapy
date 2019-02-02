import sys
from functools import lru_cache
sys.setrecursionlimit(2500)


# With recursion
@lru_cache(maxsize=None)
def longest_palim(l, r):
  if l == r:
    return 1
  
  if l  > r :
    return 0

  if text[l] == text[r]:
    return longest_palim(l+1, r-1) + 2
  else:
    return max(longest_palim(l, r-1), longest_palim(l+1, r))


# With Dynamic Programming
dp_table = [[0]*1001 for i in range(1001)]
for i in range(1001):
  dp_table[i][i] = 1
def longest_palim_dp(text):
  global dp_table

  if len(text) <= 1:
    return len(text)

  length = len(text)

  for offset in range(1, length+1):
    for i_left in range(length-offset):
      i_right = i_left + offset
      if text[i_left] == text[i_right]:
        dp_table[i_left][i_right] = 2 + (dp_table[i_left+1][i_right-1] if i_left < i_right - 1 else 0)
      else:
        dp_table[i_left][i_right] = max(dp_table[i_left+1] [i_right], dp_table[i_left] [i_right-1])

  return dp_table[0][length-1]


from sys import stdin, stdout

num_cases = int(stdin.readline())
for t in range(num_cases):
  text = stdin.readline().strip()

  # Memoization
  # print(longest_palim(0, len(text)-1))
  # longest_palim.cache_clear()

  # Dynamic Program
  stdout.write("{}\n".format(longest_palim_dp(text)))