import bisect 
from math import fabs

def index(a, x):
  i = bisect.bisect_left(a, x)
  if i != len(a) and a[i] == x:
    return i
  return -1

while True:
  try:
    n = int(input())
    line = input()
    m = int(input())
    array = []
    for i in line.split():
      bisect.insort_right(array, int(i))

    sol = None
    min_diff = 10000000

    for i in range(len(array)) :
      j = index(array[i+1:], m - array[i])
      if j >= 0:
        j += i + 1
        diff = array[i] - array[j]
        
        if diff < 0:
          diff *= -1

        if diff < min_diff:
          min_diff = diff
          sol = (i, j)
    
    b_i = array[sol[0]]
    b_j = array[sol[1]]
    print("Peter should buy books whose prices are {} and {}.".format(b_i, b_j))
    print()
    input()
  except(EOFError):
    break



  