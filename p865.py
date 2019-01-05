from os import linesep

num_tests = int(input())

for t in range(num_tests):
  try:
    if t == 0:
      input()
    text = str(input())
    sub = str(input())

    mapping = {k:v for k,v in zip(text, sub)}
    out = []
    while True:
      line = str(input())
      if line == "" :
        print(sub)
        print(text)
        print(linesep.join(out))
        print()
        break
      else:
        out.append("".join([mapping[x] if x in mapping else x for x in line]))
  except(EOFError):
    print(sub)
    print(text)
    print(linesep.join(out))
    break