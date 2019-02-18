from sys import stdin, stdout
from operator import itemgetter

cases = int(stdin.readline())
for c in range(cases):
  text = stdin.readline().strip().lower()

  text = [ch for ch in text if ch.isalpha()]
  freq = {}
  max_f = 0
  for ch in text:
    if not ch in freq:
      freq[ch] = 1
    else:
      freq[ch] += 1
    if freq[ch] > max_f:
      max_f = freq[ch]

  chars = []
  for key, f in freq.items():
    if f == max_f:
      chars.append(key)
      
  stdout.write("{}\n".format("".join(sorted(chars))))