import math 
def get_one_digit_factors(n):
  
  candidates = [2, 3, 5, 7]
  factors = [0, 0, 0, 0]
  for i, candidate in enumerate(candidates):
    while n % candidate == 0:
      n = n // candidate
      factors[i] += 1 
  if n != 1:
    raise ValueError("two digits factors")
  return factors


num_cases = int(input())

for t in range(num_cases):
  num = int(input())

  if num >= 0 and num < 10:
    print(num)
    continue

  try:
    factors = get_one_digit_factors(num)

    num_2s = 0
    num_3s = 0
    num_4s = 0
    num_5s = factors[2]
    num_6s = 0
    num_7s = factors[3]
    num_8s = factors[0] // 3
    factors[0] %= 3
    num_9s = factors[1] // 2
    factors[1] %= 2

    if factors[1] == 0:
      if factors[0] == 1:
        num_2s += 1
      elif factors[0] == 2:
        num_4s += 1
    else:
      if factors[0] == 1:
        num_6s += 1
      elif factors[0] == 2:
        num_2s += 1
        num_6s += 1
      else:
        num_3s += 1

    digits = ["2"]*num_2s + ["3"]*num_3s + ["4"]*num_4s + ["5"]*num_5s +  ["6"] * num_6s + ["7"]*num_7s + ["8"] * num_8s + ["9"] * num_9s
    print("".join(digits))
  except(ValueError):
    print("-1")
