groups = [
  "WXYZ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"
]

table = {}

for i, group in enumerate(groups):
  for ch in group:
    table[ch] = str(i)

while True:
  try:
    text = str(input())
    out = list(map(lambda x: table[x] if x in table else x, text))
    print("".join(out))
  except EOFError:
    break
