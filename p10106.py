while True:
  try:
    x = int(input())
    y = int(input())
    print(x*y)
  except EOFError:
    break