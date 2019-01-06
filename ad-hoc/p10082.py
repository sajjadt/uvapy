#!/usr/bin/python3

rows = [
  "`1234567890-=",
  "QWERTYUIOP[]\\",
  "ASDFGHJKL;'",
  "ZXCVBNM,./"
]
mapping = [' '] * 256

for row in rows:
  for i in range(1, len(row)):
    mapping[ord(row[i])] = row[i-1]

while True:
  try:
    text = input()
    print("".join( mapping[ord(ch)] for ch in text))

  except EOFError:
    break

