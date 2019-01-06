from math import sqrt

while True:
  num = int(input())
  if num == 0:
    break
  div = sqrt(num)

  # Only way for having odd number of divisors is if the number can be formed:
  # of p_i ^ 2n_i * p_j ^ 2n_j * ...

  print("yes" if div == int(div) else "no")


