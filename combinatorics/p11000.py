fib = [1, 1]
bees = [0, 1, 2]
for i in range(101):
  fib.append(fib[-1] + fib[-2])
  bees.append(bees[-1] + fib[-1])

while(True):
  n = int(input())

  if n == -1:
    break
  
  print("{} {}".format(bees[n], bees[n+1]))