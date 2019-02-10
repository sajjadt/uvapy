from sys import stdin, stdout
while True:
  n = int(stdin.readline())

  if n == 0:
    break
  
  spent = []
  for i in range(n):
    spent.append(float(stdin.readline())*100)

  spent.sort(reverse=True)
  total = sum(spent)

  exchange = 0
  q, r = divmod(total, n)
  if r == 0:
    # spending can be divided equally
    for i in range(n):
      diff = spent[i] - q
      if diff > 0:
        exchange += diff
      else:
        break
  else:
    # spending can not be divided equally
    p = 0 
    #number of people who can keep a penny and save on exchange
    for i in range(n):
      diff = spent[i] - q
      if diff > 0:
        exchange += diff
        p += 1
      else:
        break
    
    p = min(p, r)
    exchange -= p
  
  stdout.write("${:.2f}\n".format(exchange/100))


