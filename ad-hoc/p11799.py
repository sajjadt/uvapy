num_tests = int(input())

for test in range(num_tests):
  nums = list(map(int, input().split()))
  print("Case {}: {}".format(test + 1, max(nums)))