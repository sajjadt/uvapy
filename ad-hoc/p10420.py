from sys import stdin, stdout

freq = {}
num_women = int(input())
for i in range(num_women):
  line = stdin.readline().strip().split()
  country = line[0]
  if not country in freq:
    freq[country] = 1
  else:
    freq[country] += 1

for pair in sorted(freq.items()):
  stdout.write("{} {}\n".format(pair[0], pair[1]))