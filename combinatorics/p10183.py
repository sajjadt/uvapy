from bisect import bisect_right, bisect_left

def find_ge_index(a, x):
  'Find leftmost value greater than or equal to x'
  i = bisect_left(a, x)
  if i != len(a):
    return i
  raise ValueError

def find_le_index(a, x):
  'Find rightmost value less than or equal to x'
  i = bisect_right(a, x)
  if i:
    return i-1
  raise ValueError


# Fill the table
fib_table = []
limit = pow(10, 100)

fib_table.append(1)
fib_table.append(2)
current = fib_table[1]

while current < limit:
  current = fib_table[-1] + fib_table[-2]
  fib_table.append(current)


while True:
  s, e = list(map(int, input().split()))
  if [s, e] == [0, 0]:
    break

  # Left-most occurance of s
  s_i = find_ge_index(fib_table, s)
  # Right-most occurance of e 
  e_i = find_le_index(fib_table, e)

  print(e_i - s_i + 1)