from sys import stdin, stdout

def to_base(num, base):

  def get_digit(val):
    return str(val) if val < 10 else chr(ord('A') + val - 10)

  res = []
  while num >= base:
    num, rem = divmod(num, base)
    res.append(get_digit(rem))
  res.append(get_digit(num))
  return res[::-1]

while True:
  
  line = stdin.readline()
  if line == "":
    break
  num, base_from, base_to = line.strip().split()

  num = int(num, int(base_from))
  out = to_base(num, int(base_to))

  if len(out) > 7:
    # error: cannot fit in display
    stdout.write("  ERROR\n")
  else:
    stdout.write("{}\n".format("".join(out).rjust(7)))
  