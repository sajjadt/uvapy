
buffer = []
def get_next_int(n):
  ''' Returns a list contains next n integers read from the console '''
  global buffer

  while len(buffer) < n:
    inp = input()
    if inp == "" :
      continue
    else:
      buffer += list(map(int, inp.split()))
      
  ret =  buffer[0:n]
  buffer = buffer[n:]
  
  return ret
    
while True:
  len_seq = (get_next_int(1))[0]
  if len_seq == 0:
    break

  profit = [0] * len_seq


  numbers = list(map(int, get_next_int(len_seq)))

  profit[-1] = numbers[-1]
  for i in reversed(range(0, len_seq - 1)):
    profit[i] = max(numbers[i], numbers[i] + profit[i+1])
  
  if (max(profit) > 0):
    print("The maximum winning streak is {}.".format(max(profit)))
  else:
    print("Losing streak.")
