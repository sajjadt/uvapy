def calc_base_cost(num, base, cost):

  res = 0
  while num >= base:
    num, rem = divmod(num, base)
    res += cost[rem]
  res += cost[num]
  return res

from sys import stdin, stdout

num_cases = int(stdin.readline().strip())
for c in range(num_cases):
  # Get printing cost
  cost = []
  for i in range(4):
    cost += list(map(int, stdin.readline().strip().split()))
  if c > 0:
    stdout.write("\n")
  stdout.write("Case {}:\n".format(c+1))
  n = int(stdin.readline().strip())
  for i in range(n):
    number = int(stdin.readline().strip())
    base_cost_arr = [calc_base_cost(number, b, cost) for b in range(2, 37)]
    min_val = min(base_cost_arr)
    indices = [i+2 for i, v in enumerate(base_cost_arr) if v == min_val]
    stdout.write("Cheapest base(s) for number {}: {}\n".format(number, " ".join(map(str, indices))))

