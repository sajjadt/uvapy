
# f(n) = number of valid sequencess with n items
# f(n) =  {"attaching n to"}  f(n-2) +  {"attaching n-1 to "} f(n-3) 

LIMIT = 76 + 1
f_table = [0, 1, 2, 2]
for i in range(LIMIT):
  f_table.append(f_table[-2] + f_table[-3])

while True:
  try:
    n = int(input())
    print(f_table[n])
  except(EOFError):
    break
