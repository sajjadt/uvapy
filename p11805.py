num_tests = int(input())

for i in range(num_tests):
  N, K, P = list(map(int, input().split()))
  sol = (K + P) % N
  if sol == 0:
    sol = N

  print("Case {}: {}".format(i+1, sol))