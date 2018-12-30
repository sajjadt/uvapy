from math import sqrt

done = False
print("PERFECTION OUTPUT")
while True:
  line = list(map(int, input().split()))

  for num in line:
    if num == 0:
      done = True
      break
    else:

      if num > 1:
        root = int(sqrt(num)) + 1
        total = 1
        for i in range(2, root):
          if num % i == 0:
            total += i
            t = num // i
            if t != i:
              total += t
        
        if total == num:
          result = "PERFECT"
        elif total < num:
          result = "DEFICIENT"
        else:
          result = "ABUNDANT"
      else:
        result = "DEFICIENT"
      print("{:>5}  {}".format(num, result))

  if done:
    break
print("END OF OUTPUT")
  
  