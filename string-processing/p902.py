from operator import itemgetter

while True:
  try:

    # Tedious input parsing
    line = input().strip()
    while line == "":
      line = input().strip()
    
    line = line.split()
    if len(line) == 2:
      n = int(line[0])
      text = line[1]
    else:
      n = int(line[0])
      text = input().strip()
      while text == "":
        text = input().strip()

    freq_dic = {}
    for i in range(len(text) - n + 1):
      substr = text[i:i+n]
      if substr in freq_dic:
        freq_dic[substr] += 1
      else:
        freq_dic[substr] = 1
    key_max = max(freq_dic.keys(), key=(lambda k: freq_dic[k]))
    print(key_max)

  except(EOFError):
    break
