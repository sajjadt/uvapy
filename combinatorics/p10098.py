# 10098 - Generating Fast
from sys import stdin, stdout

# This function does not produce the words in sorted order. However it is in place.
def gen_permuation(letters, start_index, current_str):
  if start_index >= len(letters):
    yield current_str
  else:
    unique_letters = set()
    for i in range(start_index, len(letters)):
      if not letters[i] in unique_letters:
        unique_letters.add(letters[i])
        if i != start_index:
          letters[start_index], letters[i] = letters[i], letters[start_index]
        yield from gen_permuation(letters, start_index + 1, current_str + letters[start_index])
        if i != start_index:
          letters[start_index], letters[i] = letters[i], letters[start_index]


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
  word = stdin.readline().strip()
  
  # word = list(word)
  # for word in sorted(gen_permuation(word, 0, "")):
  #   stdout.write("{}\n".format(word))
  # print()

  word = sorted(word)
  for word in gen_permuation_sorted(word, ""):
    stdout.write("{}\n".format(word))
  print()


