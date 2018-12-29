num_tests = int(input())

for test in range(num_tests):
  num = str(input())
  if num == "1" or num == "4" or num == "78":
    print("+")
  elif num[-2:] == "35":
    print("-")
  else:
    print("*" if num[0] == "9" else "?")
