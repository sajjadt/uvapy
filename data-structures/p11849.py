from sys import stdin, stdout

sols = []
while True:
  n, m = list(map(int, stdin.readline().strip().split()))

  if n == m == 0:
    break
  
  jack_cds = set()
  for i in range(n):
    jack_cds.add(int(stdin.readline().strip()))
  
  sol = 0
  for i in range(m):
    if int(stdin.readline().strip()) in jack_cds:
      sol += 1
  sols.append(sol)

stdout.writelines("%s\n" % l for l in sols)
      