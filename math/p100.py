#!/usr/bin/python3

# UVA 100: 3n+1 problem

LIMIT = 1000001
solutions = {}
solutions[0] = 0
solutions[1] = 1 

def calc_and_get(index):
  global solutions

  if index <= 0:
    return

  if index in solutions:
    return solutions[index]
  else:
    if index % 2 == 0:
      val = calc_and_get(index / 2) + 1
    else:
      val = calc_and_get(3 * index + 1) + 1
    solutions[index] = val
  return val

for i in range(LIMIT):
  calc_and_get(i)


while True:
  try:
    line = input()
    s, e = map(int, line.split())
    max_val = -1
    for i in range(min(e, s), max(e, s)+1, 1):
      if solutions[i] > max_val:
        max_val = solutions[i]
    print(str(s) + " " + str(e) + " " + str(max_val))
  except EOFError:
    break

