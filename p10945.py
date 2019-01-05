
punctuations = ".,!? "

while True:
  line = str(input())
  if line == "DONE":
    break

  is_palindrome = True
  len_l = len(line)
  i = 0
  j = len_l - 1
  while i < j:
    if line[i] in punctuations:
      i += 1
      continue
    if line[j] in punctuations:
      j -= 1
      continue
    
    if line[i].lower() != line[j].lower():
      is_palindrome = False
      break
    
    i += 1
    j -= 1
  
  if is_palindrome:
    print("You won't be eaten!")
  else:
    print("Uh oh..")