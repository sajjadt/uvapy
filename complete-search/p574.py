from collections import OrderedDict

def count_sumup(acc, target, numbers, i, marked):
  
  if acc >= target:
    # No point to continue beyond this point
    if acc == target:
      yield "+".join(str(numbers[i]) for i,v in enumerate(marked) if v == True) 
    return 
  
  if i >= len(numbers):
    return
  
  marked[i] = True
  yield from count_sumup(acc+numbers[i], target, numbers, i+1, marked) 
  marked[i] = False
  yield from count_sumup(acc, target, numbers, i+1, marked)
    
t = 1
while True:
  inputs = list(map(int, input().split()))
  if inputs[0] == inputs[1] == 0:
    break

  target = inputs[0]
  numbers = inputs[2:]

  numbers.sort(reverse=True)
  marked = [False]*len(numbers)
  sol = list(OrderedDict.fromkeys(count_sumup(0, target, numbers, 0, marked)))

  print("Sums of {}:".format(target))
  print("\n".join(sol) if len(sol) > 0 else "NONE")
  
