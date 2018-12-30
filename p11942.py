num_tests = int(input())

print("Lumberjacks:")
for i in range(num_tests):
  in_arr = list(map(int, input().split()))
  
  ordered = True
  if len(in_arr) > 2:
    for i in range(len(in_arr) - 2):
      if in_arr[i+1] > in_arr[i] and in_arr[i+1] > in_arr[i+2]:
        ordered = False
        break
      if in_arr[i+1] < in_arr[i] and in_arr[i+1] < in_arr[i+2]:
        ordered = False
        break
  
  print("Ordered" if ordered else "Unordered")
