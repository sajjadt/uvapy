from math import sqrt

num_tests = int(input())

for t in range(num_tests):
  text = str(input())

  len_t = len(text)
  sqrt_t = int(sqrt(len_t))

  if sqrt_t*sqrt_t != len_t:
    print("INVALID")
  else:
    out = ""
    for j in range(0, sqrt_t):
      for i in range(0, len_t, sqrt_t):
        out += text[i+j]
    print(out)

