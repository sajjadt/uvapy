while True:
  try:
    print(str(input()))
  except EOFError:
    break
  