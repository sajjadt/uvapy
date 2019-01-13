from sys import stdin
from collections import Counter 

words_set = Counter()
words = []

while True:
  line = stdin.readline().strip()
  if line == "#":
    break

  for word in line.split():
    sorted_word = "".join(sorted(word.lower()))
    if len(word) >= 1:
      words_set[sorted_word] += 1
    words.append((word, sorted_word))

a_words = []
for word, sorted_word in words:
  if not sorted_word in words_set or words_set[sorted_word] < 2:
    a_words.append(word)

print("\n".join(sorted(a_words)))
