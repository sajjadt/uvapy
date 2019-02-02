# Every hand shake divides the problem into two  subproblem
# We derive the Catalan sequence from the recursion
catalan = [0, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440]

first = True
while True:
  try:
    line = input().strip()
    while line == "":
      line = input().strip()
    n = int(line)
    if first:
      first = False
    else:
      print()

    print(catalan[n])
    
  except(EOFError):
    break