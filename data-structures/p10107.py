import bisect 

numbers = []
num_items = 0
while True:
  try:
    number = int(input())
    bisect.insort_right(numbers, number)
    num_items += 1

    if num_items & 1:
      print(numbers[num_items//2])
    else:
      print( (numbers[num_items//2] + numbers[num_items//2-1]) // 2)
  except(EOFError):
    break