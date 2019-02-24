from sys import stdin, stdout

while True:
  line = stdin.readline()

  if line == "":
    break

  coeffs = list(map(int, line.strip().split()))
  
  out = []
  for x in map(int, stdin.readline().strip().split()):
    out.append(sum(c*(x**i) for i, c in enumerate(reversed(coeffs))))
  
  stdout.write("{}\n".format(" ".join(map(str, out))))