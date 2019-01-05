num_tests = int(input())

for t in range(num_tests):
  enc_words = list(map(str, input().split()))
  dec_word = str(input())

  possible_keys = set()

  for word in enc_words:
    if len(word) == len(dec_word):
      diff = set(map(lambda x:(ord(x[0]) - ord(x[1]) + 26) % 26, zip(word, dec_word)))
      if len(diff) == 1:
        possible_keys = possible_keys.union(diff)

  print("".join(sorted(map(lambda x: chr(x + ord('a')), possible_keys))))
  