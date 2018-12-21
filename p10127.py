

# Idea is to avoid doing expensive calculations on the large numbers. Instead
# play with the reminders of the operation, as wee keep adding "1"s.

while True:
  try:
    number = str(input())
    
    answer = len(number)
    smallest = int("1" * len(number))

    number = int(number)
    rem = smallest - number
    while rem != 0:
      rem = (rem * 10 + 1) % number
      answer += 1

    print(answer)
  except EOFError:
    break
  