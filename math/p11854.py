from sys import stdin, stdout

while True:
  numbers = list(map(int, stdin.readline().strip().split()))
  if numbers == [0, 0, 0]:
    break

  numbers.sort()
  if numbers[0]**2 + numbers[1]**2 == numbers[2]**2:
    stdout.write("right\n")
  else:
    stdout.write("wrong\n")
   
    