from math import sqrt

def chunks(l, n):
  """Yield successive n-sized chunks from l."""
  for i in range(0, len(l), n):
    yield l[i:i + n]

num_cases = int(input())

for t in range(num_cases):
  text = input()

  text = [x for x in text if x.isalpha()]
  len_t = len(text)

  k = int(sqrt(len_t))

  is_magic = True
  if k == 0:
    pass
  elif k*k != len_t:
    is_magic = False
  elif text != text[::-1]:
    is_magic = False
  else:
    # check symmetric
    text_2d = [x for x in chunks(text, k) ]
    for i in range(k):
      for j in range(i+1, k):
        if text_2d[i][j] != text_2d[j][i]:
          is_magic = False
          break
  
  print("Case #{}:".format(t+1))
  if is_magic:
    print(k)
  else:
    print("No magic :(")

