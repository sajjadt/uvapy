from sys import stdin, stdout

while True:
  text = stdin.readline()
  if text == "":
    break
  
  l1 = len(text)
  text = text.lstrip()
  offset = l1 - len(text)
  text = text.rstrip()

  stack = []
  valid = True

  index = 1
  i = 0 
  while i < len(text):
    ch = text[i]
    if ch in "[({<":
      if ch == "(":
        if i < len(text) -1  and text[i+1] == "*":
          stack.append("(*")
          i += 1
        else:
          stack.append("(")
      else:
        stack.append(ch)

    elif ch in "*])}>":
      if ch == "*":
        if i < len(text) -1  and text[i+1] == ")":
          i += 1
          if len(stack) == 0:
            valid = False
            break
          t_ch = stack.pop()
          # match with (*
          if t_ch !=  "(*":
            valid = False
            break
      else:
        if len(stack) == 0:
          valid = False
          break
        t_ch = stack.pop()
        if t_ch == "[" and ch != "]":
          valid = False
          break
        if t_ch == "{" and ch != "}":
          valid = False
          break
        if t_ch == "<" and ch != ">":
          valid = False
          break
        if t_ch == "(" and ch != ")":
          valid = False
          break
        if t_ch == "(*" and ch != "*)":
          valid = False
          break
        
    index += 1
    i += 1
  
  # check stack is empty
  valid = valid and len(stack) == 0
  
  stdout.write("{}\n".format("YES" if valid else "NO {}".format(index + offset)))