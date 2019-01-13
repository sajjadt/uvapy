# 195 - Anagrams
# See combinatorics/p10098.py

from sys import stdin, stdout
import functools 

# Ordering: AaBbCcDd
def sorted_by(a, b):
  if abs(ord(a) - ord(b)) == 32:
    return ord(a) - ord(b)
  else:
    # normalize to lower
    return ord(a.lower()) - ord(b.lower())

cmp_function = functools.cmp_to_key(sorted_by)

def gen_permuation_sorted(letters, current_str):
  if len(letters) == 0:
    yield current_str
  else:
    unique_letters = set()
    for i in range(len(letters)):
      if not letters[i] in unique_letters:
        unique_letters.add(letters[i])
        yield from gen_permuation_sorted(letters[:i]+letters[i+1:], current_str + letters[i])
  
num_tests = int(input())
for i in range(num_tests):

  words = stdin.readline().strip()
  words = sorted(words, key=cmp_function)
  
  for word in gen_permuation_sorted(word, ""):
    stdout.write("{}\n".format(word))
