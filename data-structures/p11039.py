num_tests = int(input())

for test in range(num_tests):
  num_blocks = int(input())
  blocks = []
  for i in range(num_blocks):
    block = int(input())
    if block > 0:
      blocks.append((block, 1))
    else:
      blocks.append((-1*block, -1))
  
  blocks = sorted(blocks, key=lambda x: x[0])
  
  if len(blocks) < 1:
    total = 0
  else:
    total = 1
    sign = blocks[0][1]
    for block in blocks[1:]:
      if block[1] != sign:
        sign *= -1
        total += 1
  print(total)
