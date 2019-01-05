
hello_table = { 
  "HELLO": "ENGLISH",
  "HOLA": "SPANISH",
  "HALLO": "GERMAN",
  "BONJOUR": "FRENCH",
  "CIAO": "ITALIAN",
  "ZDRAVSTVUJTE": "RUSSIAN"
}

case_no = 1
while True:
  word = str(input())

  if word == "#":
    break

  if word in hello_table:
    print("Case {}: {}".format(case_no, hello_table[word]))
  else:
    print("Case {}: {}".format(case_no, "UNKNOWN"))
  
  case_no += 1
  
  
