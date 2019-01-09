import re

while True:
  try:
    text = str(input())
    print(len(re.findall("[a-zA-Z]+", text)))
    
  except(EOFError):
    break