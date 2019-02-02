fingers_dic = [
  '',
  'qaz',
  'wsx',
  'edc',
  'rfvtgb',
  ' ',
  ' ',
  'yhnujm',
  'ik,',
  'ol.',
  'p;/'
]


from sys import stdin, stdout
buffer = []
def get_next_int(n):
  ''' Returns a list contains next n integers read from the console '''
  global buffer

  while len(buffer) < n:
    inp = stdin.readline()
    if inp == "" :
      continue
    else:
      buffer += list(map(int, inp.split()))
      
  ret =  buffer[0:n]
  buffer = buffer[n:]
  
  return ret

case = 1
while True:
  try:
    f, n = list(map(int, input().split()))
    missing_fingers = get_next_int(f)
    
    missing_letters = [False] * 256
    for i in missing_fingers:
      if i <= 10:
        for ch in fingers_dic[i]:
          missing_letters[ord(ch)] = True

    words = []
    max_len = 0
    for i in range(n):
      word = input()

      valid_word = True
      for ch in word:
        if missing_letters[ord(ch)]:
          valid_word = False
          break
      
      if valid_word:
        if len(word) > max_len:
          words = [word]
          max_len = len(word)
        elif len(word) == max_len:
          words.append(word)
        else:
          continue
      
    if len(words) > 0:
      words = sorted(list(set(words)))
      stdout.write("{}\n{}\n".format(len(words), "\n".join(words)))
    else:
      stdout.write("0\n")
    case += 1
  except(EOFError):
    break
