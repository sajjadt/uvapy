num_tests = int(input())

for i in range(num_tests):
  num = int(input())

  num *= 567
  num //= 9
  num += 7492
  num *= 235
  num //= 47
  num -= 498
  
  if num < 0:
    num *= -1
  
  num //= 10
  num %= 10
  
  print(num)