
num_correct = 0

while True:
  try:
    line = input().strip()
    l, r = line.split("=")

    if r == "?":
      continue

    if "+" in l:
      l1, l2 = l.split("+")
      if int(l1) + int(l2) == int(r):
        num_correct += 1
    else:
      l1, l2 = l.split("-")
      if int(l1) - int(l2) == int(r):
        num_correct += 1
  except(EOFError):
    break

print(num_correct)