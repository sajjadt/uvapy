
test_no = 1
while True:
  try:
    seq = input()
    table = [0 for i in range(9)]
    
    # a0 b1 c2 
    # d3 e4 f5
    # g6 h7 i8

    for ch in seq:
      if ch == "a":
        table[0] += 1
        table[1] += 1
        table[3] += 1
      elif ch == "b":
        table[0] += 1
        table[1] += 1
        table[2] += 1
        table[4] += 1
      elif ch == "c":
        table[1] += 1
        table[2] += 1
        table[5] += 1
      elif ch == "d":
        table[0] += 1
        table[3] += 1
        table[4] += 1
        table[6] += 1
      elif ch == "e":
        table[1] += 1
        table[3] += 1
        table[4] += 1
        table[5] += 1
        table[7] += 1
      elif ch == "f":
        table[2] += 1
        table[4] += 1
        table[5] += 1
        table[8] += 1
      elif ch == "g":
        table[3] += 1
        table[6] += 1
        table[7] += 1
      elif ch == "h":
        table[4] += 1
        table[6] += 1
        table[7] += 1
        table[8] += 1
      else:
        table[5] += 1
        table[7] += 1
        table[8] += 1

    table = [str(x%10) for x in table]
    print("Case #{}:".format(test_no))
    print("\n".join(
      [
        " ".join(table[0:3]),
        " ".join(table[3:6]),
        " ".join(table[6:9])
      ]
      ))

    test_no += 1
  except(EOFError):
    break