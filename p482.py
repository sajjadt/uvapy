from os import linesep

num_tests = int(input())

for i in range(num_tests):
  input()

  perms = list(map(int, input().split()))
  nums = list(map(str, input().split()))
  out = [0] * len(perms)

  for j in range(len(perms)):
    out[perms[j]-1] = str(nums[j])

  print(linesep.join(out))

  if i != num_tests - 1:
    print()
