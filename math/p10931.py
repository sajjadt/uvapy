from sys import stdin, stdout

while True:
  n = int(stdin.readline().strip())

  if n == 0:
    break

  res = 0
  bin_rep = []
  while n > 0:
    n, d = divmod(n, 2)
    res += d
    bin_rep.append(d)

  stdout.write("The parity of {} is {} (mod 2).\n".format("".join(map(str, reversed(bin_rep))), res))

