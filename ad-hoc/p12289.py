num_tests = int(input())

for test in range(num_tests):
  letter = str(input())

  if len(letter) == 5:
    print("3")
  else:
    sim_1 = 0
    sim_2 = 0

    if letter[0] == 'o':
      sim_1 += 1
    if letter[1] == 'n':
      sim_1 += 1
    if letter[2] == 'e':
      sim_1 += 1

    if letter[0] == 't':
      sim_2 += 1
    if letter[1] == 'w':
      sim_2 += 1
    if letter[2] == 'o':
      sim_2 += 1

    if sim_1 > sim_2:
      print("1")
    else:
      print("2")
