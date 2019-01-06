test_no = 0
while True:
  input_v = input().split()
  a, b = [str(x) for x in input_v]

  if a == "0" and b == "0":
    break


  result = bin(int(a, 2) * int(b, 2))[2:]

  if test_no > 0:
    print()

  print(' '*( max(len(b), len(result))-len(a)) + a)
  print(' '*( max(len(a), len(result))-len(b)) + b)
  
  # print a and b
  if len(a) > len(b):
    print(' '*(len(result)-len(a)) + '-'*len(a))
  else:
    print(' '*(len(result)-len(b)) + '-'*len(b))

  # Print the sequence
  tail_spaces = max(len(b), len(result))-len(a)
  for ch in reversed(b):
    if ch == '0':
      print_a = '0' * len(a)
    else:
      print_a = a
    print(' '*tail_spaces + print_a  )
    tail_spaces -= 1
    
  max_len = max(map(len, [result, a, b]))
  print('-'*max_len)
  print(' '*(max_len - len(result)) + result)
  test_no += 1
  
