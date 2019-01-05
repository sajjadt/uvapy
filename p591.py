
test_no = 1
while True:
  n = int(input())

  if n == 0:
    break

  H = list(map(int, input().split()))
  final_height = sum(H) // n
  moves = sum(map(lambda x: final_height - x if x < final_height else 0, H))
  
  print("Set #{}".format(test_no))
  print("The minimum number of moves is {}.".format(moves))
  print()

  test_no += 1