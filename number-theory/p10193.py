from sys import stdin, stdout

def gcd(a, b):
  while(b): 
    a, b = b, a % b 
  return a

cases = int(stdin.readline().strip())
for case in range(cases):
  a = int(stdin.readline().strip(), base=2)
  b = int(stdin.readline().strip(), base=2)
  if gcd(a, b) == 1:
    result = "Love is not all you need!"
  else:
    result = "All you need is love!"
  print("Pair #{}: {}".format(case + 1, result))
