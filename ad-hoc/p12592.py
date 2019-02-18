from sys import stdin, stdout

N = int(stdin.readline().strip())

slogans = {}
for i in range(N):
  first = stdin.readline().strip()
  second = stdin.readline().strip()
  slogans[first] = second

Q = int(stdin.readline().strip())
for i in range(Q):
  first = stdin.readline().strip()
  stdout.write("{}\n".format(slogans[first]))