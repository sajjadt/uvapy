def to_base_10(num, b):
  res = ""
  while num >= b:
    num, rem = divmod(num, b)
    res += str(rem)
  res += str(num)
  return res[::-1]

while True:
  line = str(input())

  if line == "0":
    break
  
  b, p, m = line.split()
  b = int(b)
  
  p = int(p, b)
  m = int(m, b)
  res = p % m

  print (to_base_10(res, b))
  
