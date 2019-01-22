
def input_gen(max_in):
  read = 0  
  while True:
    line = list(map(int, input().split()))
    for l in line:
      yield(l)
      read += 1
      if read >= max_in:
        return 

def flip_sort(arr):
  num_flips = 0
  for i in range(1, len(arr)):
    j = i
    while j >= 1 and arr[j-1] > arr[j]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
      num_flips += 1
      j -= 1
  return num_flips

while True:
  try:
    l = ""
    while l == "":
      l = input().strip()
    n = int(l)

    G = input_gen(n)
    numbers = [0] * n
    for i in range(n):
      numbers[i] = next(G)
      
    print("Minimum exchange operations : {}".format(flip_sort(numbers)))
  except(EOFError):
    break
