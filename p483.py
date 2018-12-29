while True:
  try:
    line = input()
    word = ""
    out = ""
    for ch in line:
      if ch == " ":
        if len(word) > 0:
          out += word[::-1]
          word = ""
        out += ch
      else:
        word += ch
    out += word[::-1]
    print(out)
  except EOFError:
    break