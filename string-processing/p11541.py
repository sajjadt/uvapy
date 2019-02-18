num_cases = int(input())

for c in range(num_cases):
  coded = input().strip()
  out = []
  i = 0
  while i < len(coded):
    ch = coded[i]
    i += 1
    count = 0
    while i < len(coded) and  coded[i].isdigit():
      count = count * 10 + int(coded[i])
      i += 1
    out += ([ch] * count)
  
  print("Case {}: {}".format(c+1, "".join(out)))