num_tests = int(input())

for test in range(num_tests):
  num_chars = int(input())
  ch_map = {}
  
  for i in range(num_chars):
    line = input().split()
    ch, w = line[0], int(line[1])
    ch_map[ch] = w
  
  num_lines = int(input())
  total = 0

  for i in range(num_lines):
    line = str(input())
    total += sum(map(lambda x: ch_map[x] if x in ch_map else 0, line))
  
  print("{0:.2f}$".format(total/100))
