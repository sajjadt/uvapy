from operator import itemgetter
from sys import stdin, stdout

num_tests = int(input())

for t in range(num_tests):
  input()
  
  if t > 0:
    stdout.write("\n")

  w, n = list(map(int, stdin.readline().strip().split()))
  words = []
  freqs = [0] * n
  for i in range(n):
    words.append(list(input().strip()))
  
  for i, p in enumerate(words):
    num_a = num_c = num_t = num_g = 0
    for ch in p:
      if ch == "A":
        num_a += 1
      elif ch == "C":
        num_c += 1
      elif ch == "T":
        num_t += 1
      else:
        num_g += 1

    count = 0
    for ch in p:
      if ch == "A":
        num_a -= 1
      elif ch == "C":
        count += (num_a)
        num_c -= 1
      elif ch == "G":
        count += (num_a + num_c)
        num_g -= 1
      else:
        count += (num_a + num_c +  num_g)
        num_t -= 1
    freqs[i] = count 

  res = ["".join(y) for f, y in sorted(zip(freqs, words), key=itemgetter(0))]
  stdout.write("\n".join(res)+"\n")
