def foo(numbers, path, index, cur_val, target):
  
  if index == len(numbers):
    return cur_val, path

  # No point in continuation
  if cur_val > target:
    return -1, ""

  
  sol_1 = foo(numbers, path+"1", index+1, cur_val+numbers[index], target)

  # Found the solution. Do not continue.
  if sol_1[0] == target:
    return sol_1
  
  sol_2 = foo(numbers, path+"0", index+1, cur_val, target)
  if sol_2[0] == target:
    return sol_2

  if sol_1[0] == -1 or sol_1[0] > target:
    if sol_2[0] == -1 or sol_2[0] > target:
      return -1, ""
    else:
      return sol_2
  else:
    if sol_2[0] == -1 or sol_2[0] > target or sol_1[0] > sol_2[0]:
      return sol_1
    else:
      return sol_2

while True:
  try:
    line = list(map(int, input().split()))
    N = line[1]
    Target = line[0]
    numbers = line[2:]

    if sum(numbers) <= Target:
      print((" ".join(map(str, numbers))) + " sum:{}".format(sum(numbers)))
    else:
      sol, path = foo(numbers, "", 0, 0, Target)
      print(" ".join([str(p) for p, v in zip(numbers, path) if v=="1"]) + " sum:{}".format(sol))

  except(EOFError):
    break