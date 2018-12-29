LIMIT = 1000000
solution = [0, 0, 0, 0, 1]

k = 2
for i in range(5, LIMIT + 1):
  solution.append(solution[-1] + k)
  k += (i -1 ) // 2

while True:
  n = int(input())
  if n < 3:
    break
  print(solution[n])