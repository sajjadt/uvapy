lines = []
while True:
  try:
    lines.append(input())
  except(EOFError):
    break
lines = lines[::-1]
line_lens = map(len, lines)
max_len = max(line_lens)

out_lines = ["" for i in range(max_len)]

for line in lines:
  for c, char in enumerate(line):
    out_lines[c] += char
  for c in range(len(line), max_len):
    out_lines[c] += " "
      
print("\n".join(map(str, out_lines)))