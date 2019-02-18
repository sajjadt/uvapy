while True:
  try:
    n, b = list(map(int, input().split()))

    # With b bits, it is possible to represet 1 file with 0 bits,
    # 2 files with 1 bit, 4 files with 2 bits, etc.
    # total = 2**(b+1) - 1

    if n > 2**(b+1) - 1:
      print("no")
    else:
      print("yes")
  except(EOFError):
    break