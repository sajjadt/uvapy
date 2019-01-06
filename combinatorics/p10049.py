from bisect import bisect_right, bisect_left

def find_le_index(a, x):
  'Find rightmost value less than or equal to x'
  i = bisect_right(a, x)
  if i:
    return i-1
  raise ValueError

LIMIT = 673365 + 1

ftable = [i for i in range(LIMIT)]
ftable[1] = 1
ftable[2] = 2
j = 3
while j < LIMIT:
  ftable[j] = ftable[j-1] + find_le_index(ftable, j-1)
  j += 1

while True:
  num = int(input())
  if num == 0:
    break
  print(find_le_index(ftable, num))