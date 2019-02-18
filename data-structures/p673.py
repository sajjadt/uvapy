from sys import stdin, stdout
num_cases = int(stdin.readline().strip())

for c in range(num_cases):
  text = stdin.readline().strip().strip()
  stack = []
  valid = True
  
  for ch in text:
    if ch in "[(":
      stack.append(ch)
    elif ch in "])":
      if len(stack) == 0:
        valid = False
        break
      t_ch = stack.pop()
      if ch == "]" and t_ch != "[":
        valid = False
        break
      if ch == ")" and t_ch != "(":
        valid = False
        break
    else:
      valid = False
  # check stack is empty
  valid = valid and len(stack) == 0
  stdout.write("{}\n".format("Yes" if valid else "No"))