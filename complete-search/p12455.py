num_tests = int(input())

def create_bar(target, bars):
  is_picked = [False] * len(bars) 

  def make_bar(i, sum_so_far):
    if sum_so_far == target:
      yield is_picked
    else:
      if i < len(bars):
        if sum_so_far + bars[i] <= target:
          is_picked[i] = True
          yield from make_bar(i+1, sum_so_far + bars[i])
          is_picked[i] = False
          yield from make_bar(i+1, sum_so_far)
        else:
          is_picked[i] = False
          yield from make_bar(i+1, sum_so_far)
      else:
        return 

  yield from make_bar(0, 0)

for test in range(num_tests):
  target_len  = int(input())
  num_bars = int(input())
  bars = list(map(int, input().split()))

  if any(create_bar(target_len, bars)):
    print("YES")
  else:
    print("NO")
