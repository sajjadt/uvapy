
mem = {}

# With no borrowing
def cola(n):
  if n < 3:
    return n

  if n in mem:
    return mem[n]

  d, r = divmod(n, 3)
  mem[n] =  n - r + cola(d+r)

  return mem[n]

while True:
  try:
    n = int(input())
    print(cola(n+1) - 1)  # borrow and return a bottle
  except(EOFError):
    break