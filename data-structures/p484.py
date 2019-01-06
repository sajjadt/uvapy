freq_map = {}
unique_numbers = []

while True:
  try:
    numbers = list(map(int, input().split()))    
    for number in numbers:
      if number in freq_map:
        freq_map[number] += 1
      else:
        freq_map[number] = 1
        unique_numbers.append(number)
  except EOFError:
    break
    
for number in unique_numbers:
      print("{} {}".format(number, freq_map[number]))