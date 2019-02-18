r_fib = {}
LIMIT = 100 + 1

fib = [1,2]
for i in range(LIMIT):
  fib.append(fib[-1] + fib[-2])

for i in range(LIMIT):
  r_fib[fib[i]] = i


num_cases = int(input())

for c in range(num_cases):
  input()
  code = list(map(int, input().split()))
  cipher = input().strip()

  out_text = [' '] * 100
  i = 0
  str_len = 0
  for ch in cipher:
    if i >= len(code):
      break
    if ch.isupper():
      out_index = r_fib[code[i]] 
      out_text[out_index] = ch
      str_len = max(str_len, out_index+1)
      i += 1
  print("".join(out_text[:str_len]))