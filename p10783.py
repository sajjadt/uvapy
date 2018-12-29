num_tests = int(input())
for test in range(num_tests):
  start = int(input())
  end = int(input())

  if start & 1 == 0:
    start += 1
  if end & 1 == 0:
    end -= 1 

  if end < start:
    total = 0
  elif end == start:
    total = start
  else:
    num_numbers = (end - start) // 2 + 1
    total = (end + start) * (num_numbers//2)
    if num_numbers % 2:
      total += (end + start) // 2
  
  print ("Case {}: {}".format(test+1, total))