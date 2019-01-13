from sys import stdin, stdout

num_tests = int(stdin.readline().strip())

for t in range(num_tests):
  num_items = int(stdin.readline().strip())
  
  numbers = [] 
  dic = {}
  curr_seq = max_seq = 0

  for i in range(num_items):
    item = int(stdin.readline().strip())
    numbers.append(item)

    if item in dic:
      if curr_seq > max_seq:
        max_seq = curr_seq

      old_val = dic[item]
      # remove items on and before item in the stream
      for v in range(i - curr_seq, old_val+1):
        del dic[numbers[v]]
        curr_seq -= 1
      dic[item] = i
      curr_seq += 1

    else:
      curr_seq += 1
      dic[item] = i
  
  if curr_seq > max_seq:
    max_seq = curr_seq
  print(max_seq)
  
