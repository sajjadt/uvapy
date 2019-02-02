from sys import stdin, stdout
case = 1

# Using stdin/stdout instead of input()/output improve runtime from 0.2s to 0.05s
while True:
  b, s = list(map(int, stdin.readline().split()))
  
  if b == s == 0:
    break
  
  min_bach_age = 63
  for i in range(b):
    age = int(stdin.readline())
    if age < min_bach_age:
      min_bach_age = age

  for i in range(s):
    stdin.readline()
  # All bachelors will get married somehow
  if s >= b:
    stdout.write("Case {}: 0\n".format(case))
  else:
    stdout.write("Case {}: {} {}\n".format(case, b - s, min_bach_age))
  case += 1
