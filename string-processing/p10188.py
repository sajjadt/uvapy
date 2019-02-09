from sys import stdin, stdout

run = 1
while True:
  num_lines = int(stdin.readline().strip())
  if num_lines == 0:
    break
  
  out_1 = ""
  out_2 = ""
  for i in range(num_lines):
    out_1 += stdin.readline()

  num_lines = int(stdin.readline().strip())
  for i in range(num_lines):
    out_2 += stdin.readline()

  remove_alpha = lambda t: "".join([ch for ch in t if ch.isdigit()])

  if out_1 == out_2:
    res = "Accepted"
  elif remove_alpha(out_1) == remove_alpha(out_2):
    res = "Presentation Error"
  else:
    res = "Wrong Answer"

  stdout.write("Run #{}: {}\n".format(run, res))
  run += 1
  