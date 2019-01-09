bit_value = [1<<i for i in reversed(range(8))]

text = str(input())
message = ""
while True:
  text = str(input()).strip()
  
  if text == "___________":
    if len(message) > 0:
      print(message)
    break  

  # remove tape 
  text = text[1:6] + text[7:-1]  
  val = sum([bit_value[i] for i, ch in enumerate(text) if ch == "o" ])
  
  if val == 10 or val == 13:
    if len(message) > 0:
      print(message)
      message = ""
    else:
      print()
    
  else:
    message += chr(val)
  