from sys import stdin, stdout

while True:
  n = int(input())

  if n == 0:
    break

  line = list(map(int, stdin.readline().strip().split()))
  local_extremas = 0
  for i in range(1, len(line) - 1):
    if line[i] > line[i-1] and line[i] > line[i+1]:
      local_extremas += 1
    if line[i] < line[i-1] and line[i] < line[i+1]:
      local_extremas += 1
  
  if line[0] > line[-1] and line[0] > line[1]:
      local_extremas += 1
  if line[0] < line[-1] and line[0] < line[1]:
    local_extremas += 1
  
  if line[0] > line[-1] and line[-2] > line[-1]:
      local_extremas += 1
  if line[0] < line[-1] and line[-2] < line[-1]:
    local_extremas += 1
  
  print(local_extremas)
