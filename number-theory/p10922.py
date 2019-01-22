from sys import stdin

def sum_digits(num):
  total = 0
  while num > 0:
    num, r = divmod(num, 10)
    total += r
  return total


while True:
  inp = stdin.readline().strip()

  if inp == "0":
    break
  
  if inp == "9":
    recursion = 1
    divides = True
  else:
    recursion = 1
    num = sum(map(int, list(inp)))
    if num % 9 == 0:
      divides = True
      while num > 9:
        num = sum_digits(num)
        recursion += 1
    else:
      divides = False

  if divides:
    print("{} is a multiple of 9 and has 9-degree {}.".format(inp, recursion))
  else:
    print("{} is not a multiple of 9.".format(inp))

