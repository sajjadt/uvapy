import re

# regex patterns
# Words that start with a, e, i, o, u - > ay
# Words that start with [a-z] - {a, e, i, o, u}
def append_ay(m):
  x = m.group(0)
  if not m.group(0)[-1].isalpha():
    replaced = m.group(0)[:-1] + 'ay' + m.group(0)[-1]
  else:
    replaced = m.group(0) + 'ay' 

  return replaced

def remove_and_append_ay(m):
  x = m.group(0)
  # Dirty hack...
  if not x[0].isalpha():
    if not x[-1].isalpha():
      replaced = x[0] + x[2:-1] + x[1] +  'ay' + x[-1]
    else:
      replaced = x[0] + x[2:] + x[1] +  'ay'   # good
  else:
    if not x[-1].isalpha():
      replaced = x[1:-1] + x[0] +  'ay' + x[-1]
    else:
      replaced = x[1:] + x[0] +  'ay'   # good

  return replaced

vowels = set(list("aeiouAEIOU"))
while True:
  try:
    line = input()

    out = ""
    i = j = 0
    while i < len(line):
      if not line[i].isalpha():
        out += line[i]
        i+=1
      else:
        j = i
        while j < len(line) and line[j].isalpha():
          j+=1
        w = line[i:j]
        if w[0] in vowels:
          out += (w + "ay")
        else:
          out += (w[1:] + w[0] + "ay")
        # i : j-1 points to a valid word
        i = j

    # Regex: bogus
    # line = re.sub(r'(?:\b|_|[0-9])[aeiouAEIOU][a-zA-Z]*(?:\b|_|[0-9])', append_ay, line)
    # line = re.sub(r'(?:\b|_|[0-9])[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z][a-zA-Z]*(?:\b|_|[0-9])', remove_and_append_ay, line)
    print(out)
  except(EOFError):
    break