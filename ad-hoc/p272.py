first = True
while True:
  try:
    line = str(input())
    out = []
    for ch in line:
      if ch == '"':
        if first:
          out.append('`')
          out.append('`')
        else:
          out.append("'")
          out.append("'")
        first = not first
      else:
        out.append(ch)

    print("".join(out))
  except EOFError:
    break
  