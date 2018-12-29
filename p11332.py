
while True:
  num = str(input())
  if num == "0":
    break
  
  while len(num) > 1:
    num = str(sum(map(int, num)))
  
  print(num)