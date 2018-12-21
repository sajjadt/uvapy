

while True:
  numbers = input().split()
  if numbers == ["0", "0"]:
    break
  
  # add and measure carrys
  i = len(numbers[0]) - 1
  j = len(numbers[1]) - 1
  
  num_couts = 0
  cout = 0
  while (i >= 0 or j >= 0):
    # ASCII table related calculations

    sum = cout + (ord(numbers[0][i]) if i >= 0 else ord('0')) + (ord(numbers[1][j]) if j >=0 else ord('0')) - 2*ord('0')
    if sum >= 10:
      cout = 1
      num_couts += 1
    else:
      cout = 0
    i -= 1
    j -= 1
  
  print(
    str(num_couts) + " carry operations." if num_couts > 1 else
    str(num_couts) + " carry operation." if num_couts == 1 else
    "No carry operation.")