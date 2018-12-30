while True:
  try:
    a, b = list(map(int, input().split()))
    print(a ^ b)
  except(EOFError):
    break