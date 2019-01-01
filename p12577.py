case = 1
while True:
  line = str(input())
  if line == "*":
    break

  hajj = "Hajj-e-Akbar" if line == "Hajj" else "Hajj-e-Asghar" 
  print("Case {}: {}".format(case, hajj))
  case += 1