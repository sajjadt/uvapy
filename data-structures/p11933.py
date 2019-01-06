while True:
  num = int(input())

  if num == 0:
    break

  a = 0
  b = 0
  turn_a = True 
  i = 0
  while num != 0:
    bit = num & 1
    num = num >> 1

    if bit == 1:
      if turn_a:
        a ^= (1 << i)
      else:
        b ^= (1 << i)
      turn_a = not turn_a
    
    i += 1
   
  print ("{} {}".format(a, b))