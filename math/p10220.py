import time
from math import factorial


def sum_digits(num):
  sum_d = 0
  while num > 0:
    num, r = divmod(num, 10)
    sum_d +=r 
  return sum_d

fact_table = [0] * 1001
fact_table[1] = 1

# s = time.time()
for i in range(2, 1001):
  fact_table[i] = i * fact_table[i-1]
e = time.time()
# print(e - s)

while True:
  try:
    inp = int(input())
    print(sum_digits(fact_table[inp]))
  except(EOFError):
    break