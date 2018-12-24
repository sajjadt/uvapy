
from math import factorial

# derangement can be proven via inclusion/exclusion
# derangement(n) = n!/2 - n!/3 + n!/4 - ....
# then it can described recursively:
# f(n) = (n-1) (f(n-1) + f(n-2))

LIMIT = 15
solution_table = [0, 0, 1, 2]
for n in range(4, LIMIT):
  solution_table.append((n-1)* (solution_table[n-1] + solution_table[n-2]))
factorial_table = [factorial(n) for n in range(LIMIT)]

num_tests = int(input())
for test in range(num_tests):
  number = int(input())
  
  if number == 0:
    break
  else:
    print(str(solution_table[number]) + "/" + str(factorial_table[number]))
   
