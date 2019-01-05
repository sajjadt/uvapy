while True:
  line = input()
  if str(line) == "0":
    break

  line = line.split()
  n, word = int(line[0]), str(line[1])
  n = len(word) // n

  out = "".join([word[i:i+n][::-1] for i in range(0, len(word), n)])
  print(out)