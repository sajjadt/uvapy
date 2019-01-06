import random
def quickselect_median(l, pivot_fn=random.choice):
  # General case
  # if len(l) % 2 == 1:
  #   return quickselect(l, len(l) // 2, pivot_fn)
  # else:
  #   return 0.5 * (quickselect(l, len(l) // 2 - 1, pivot_fn) +
  #   quickselect(l, len(l) // 2, pivot_fn))
  return quickselect(l, len(l) // 2, pivot_fn)


def quickselect(l, k, pivot_fn):
  """
  Select the kth element in l (0 based)
  :param l: List of numerics
  :param k: Index
  :param pivot_fn: Function to choose a pivot, defaults to random.choice
  :return: The kth element of l
  """
  if len(l) == 1:
    assert k == 0
    return l[0]

  pivot = pivot_fn(l)

  lows = [el for el in l if el < pivot]
  highs = [el for el in l if el > pivot]
  pivots = [el for el in l if el == pivot]

  if k < len(lows):
    return quickselect(lows, k, pivot_fn)
  elif k < len(lows) + len(pivots):
    # We got lucky and guessed the median
    return pivots[0]
  else:
    return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
   
num_tests = int(input())

for i in range(num_tests):
  numbers = list(map(int, input().split()))
  
  # Sort based median O(nlog n)
  # num_elements = numbers[0] + 1
  # numbers[0] = 0
  # numbers = sorted(numbers)
  # median = numbers[num_elements // 2]

  # Quick select median (Expected O(nlog n))
  del numbers[0]
  median = quickselect_median(numbers)
  print("Case {}: {}".format(i+1, median))