import re

# ^ matches the start of the string
# $ matches the end of the string
RE_INT = re.compile(r'^[-+]?(\d+)$')
RE_REAL = re.compile(r'^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$')

while True:
  try:
    text = str(input()).strip()

    if text == "*":
      break
    
    is_real = re.search(RE_REAL, text)
    is_int = re.search(RE_INT, text)

    if is_real and not is_int:
      print("{} is legal.".format(text))
    else:
      print("{} is illegal.".format(text))
    
  except(EOFError):
    break