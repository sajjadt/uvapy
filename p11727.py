num_tests = int(input())

for test in range(num_tests):
  a, b, c = list(map(int, input().split()))
  total = a + b + c

  min_salary = a
  if b < min_salary:
    min_salary = b
  if c < min_salary:
    min_salary = c

  max_salary = a
  if b > max_salary:
    max_salary = b
  if c > max_salary:
    max_salary = c
  
  print("Case {}: {}".format(test+1, total - min_salary - max_salary))