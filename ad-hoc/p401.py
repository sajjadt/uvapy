
reversed_letters = {
  'A' : 'A',
  'E' : '3',
  'H' : 'H',
  'I' : 'I', 
  'J' : 'L',
  'L' : 'J',
  'M' : 'M',
  'O' : 'O',
  'S' : '2', 
  'T' : 'T',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X', 
  'Y' : 'Y',
  'Z' : '5',
  '1' : '1',
  '2' : 'S',
  '3' : 'E', 
  '5' : 'Z',
  '8' : '8'
}

from sys import stdin, stdout

while True:
  try:
    string = input()



    # Ugly version with early break
    # is_palin = True
    # is_mirrored = True
    # i = 0
    # j = len(string) - 1
    # while i < j:
    #   if string[i] != string[j]:
    #     is_palin = False
    #   if (string[i] not in reversed_letters) or (string[j] != reversed_letters[string[i]]) \
    #      or (string[j] not in reversed_letters) or (string[i] != reversed_letters[string[j]]):
    #     is_mirrored = False
      
    #   i += 1
    #   j -= 1

    #   if not is_mirrored and not is_palin:
    #     break

    # if is_mirrored and len(string) & 1 == 1:
    #   c_m = string[len(string) // 2]
    #   if (c_m not in reversed_letters) or (c_m != reversed_letters[c_m]):
    #     is_mirrored = False


    # Short version
    is_palin = string == string[::-1]
    is_mirrored = string == "".join([reversed_letters.setdefault(ch, "") for ch in string[::-1]])

    outcome = "is not a palindrome" if (not is_palin and not is_mirrored) else \
      "is a regular palindrome" if (not is_mirrored and is_palin) else \
      "is a mirrored string" if (not is_palin and is_mirrored) else \
      "is a mirrored palindrome"
    
    print("{} -- {}.\n".format(string, outcome))

  except(EOFError):
    break