from collections import Counter
from sys import stdin, stdout  
import time

def print_trees(trees):
  for k, v in sorted(trees.items()):
    message = "{} {:.4f}\n".format(k, v/total*100)
    stdout.write(message)  

start = time.time()
try:
  num_tests = int(stdin.readline())
  stdin.readline()
  for i in range(num_tests):
    trees = Counter()
    total = 0
    while True:
      # Faster than input()
      line = stdin.readline().strip()
      if line == "":
        print_trees(trees)
        if i < num_tests - 1:
          print()
        break
      
      # No need to explicit check
      trees[line] += 1
      total += 1

except(EOFError):
  pass

end = time.time()
# print(end-start)