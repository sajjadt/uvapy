from sys import stdin, stdout

while True:
  line = stdin.readline()
  if line == "":
    break

  n = int(line.strip())
  row = (n+1) // 2

  last_num = 2 * (row*row) - 1
  stdout.write("{}\n".format(3*last_num - 6))