num_tests = int(input())

for i in range(num_tests):
  num_text = str(input())

  num_dec = int(num_text)
  num_hex = int(num_text, 16)

  num_dec = bin(num_dec)
  num_hex = bin(num_hex)

  # Both these are equal
  b1 = len([x for x in num_dec if x == "1"])
  b2 = len([x for x in num_hex if x == "1"])
  
  print("{} {}".format(b1, b2))
