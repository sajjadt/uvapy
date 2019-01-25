from sys import stdin, stdout

numbers = [0]*1024
while True:
  n = int(input())
  if n == 0:
    break
  
  for i in range(n):
    numbers[i] = int(stdin.readline())

  seq = [str(x) for x in numbers[0:n] if x > 0]
  if len(seq) == 0: # All zeros
    seq = ["0"]
  stdout.write(" ".join(seq) + "\n")
