from math import factorial
# import time
LIMIT = 1000

# Based on my profiling, using multiplication is 20x times faster than calling factorial function
# start = time.time()
# fact_table = [factorial(i) for i in range(LIMIT+1)]
# end = time.time()
# print(end - start)

# start = time.time()
fact_table = [1]
for i in range(1, LIMIT+1):
  fact_table.append(i*fact_table[-1])
# end = time.time()
# print(end - start)

while True:
  try:
    num = int(input())
    print("{}!".format(num))
    print(fact_table[num])
  except(EOFError):
    break