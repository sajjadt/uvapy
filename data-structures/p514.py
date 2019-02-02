from sys import stdin, stdout
while True:
  l = stdin.readline().strip()
  if l == "0":
    break
  
  n = int(l)
  in_order = [i+1 for i in range(n)]

  l = stdin.readline().strip()
  while l != "0":
    out_order = list(map(int, l.split()))
    can_do = True

    stack = []
    in_i = 0
    out_i = 0
    while out_i < n :
      # Bypass the stack (push followd by pop)
      if in_i < n and in_order[in_i] == out_order[out_i]:
        in_i += 1
        out_i += 1
      # Search the stack (pop)
      elif len(stack) > 0 and stack[-1] == out_order[out_i]:
        stack.pop()
        out_i += 1
      # Push into stack
      else:
        if in_i < n:
          stack.append(in_order[in_i])
          in_i += 1
        else:
          can_do = False
          break
    stdout.write("Yes\n" if can_do else "No\n")
    l = input().strip()
  print()