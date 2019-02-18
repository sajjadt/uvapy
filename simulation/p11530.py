mapping = [
  "abc", "def",
  "ghi", "jkl", "mno",
  "pqrs", "tuv", "wxyz",
  " "
]

key_count = {}
for key in mapping:
  for i, ch in enumerate(key):
    key_count[ch] = i + 1

cases = int(input())
for c in range(cases):
  text = input()
  count = 0
  for ch in text:
    count += key_count[ch]
  
  print("Case #{}: {}".format(c+1, count))