from itertools import permutations
# import time
from sys import stdin, stdout

# start = time.time() 
test_no = 0
while True:
  N = int(stdin.readline().strip())

  if N == 0:
    break
  
  if test_no > 0:
    stdout.write("\n")

  PERM = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  def foo(n):
  # a / b = N -> a = N * b -> a > b
    sols = []
    for b in permutations(PERM, 5):
      num_b = b[0] + 10*b[1] + 100*b[2] + 1000*b[3] + 10000*b[4]
      copy_a = num_a = n * num_b
      if num_a > 98765:
        continue
      digits = [0] * 10
      digits[b[0]] = 1
      digits[b[1]] = 1
      digits[b[2]] = 1
      digits[b[3]] = 1
      digits[b[4]] = 1

      valid_sol = True
      if num_a < 10000:
        digits[0] += 1
        if digits[0] > 1:
          valid_sol = False
      
      while valid_sol and num_a > 0:
        num_a, y = divmod(num_a, 10)
        digits[y] += 1
        if digits[y] == 2:
          valid_sol = False      
      
      if valid_sol:
        sols.append([copy_a, num_b])

    return sorted(sols)

  sols = foo(N)
  if len(sols) == 0:
    stdout.write("There are no solutions for {}.\n".format(N))
  else:
    stdout.write("\n".join(["{} / {} = {}".format(p[0], p[1] if p[1] > 9999 else "0"+str(p[1]), N) for p in sols]))
    stdout.write("\n")
  test_no += 1

# end = time.time()
# print(end - start)