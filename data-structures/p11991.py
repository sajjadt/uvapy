from sys import stdin, stdout

while True:
  try:
    line = stdin.readline()
    if len(line) == 0:
      break

    n, m = list(map(int, line.strip().split()))
    nums = {}
    for i, num in enumerate(map(int, input().split())):
      if num in nums:
        nums[num].append(i+1)
      else:
        nums[num] = [i+1]


    for q in range(m):
      k, v = list(map(int, input().split()))
      if not v in nums or len(nums[v]) < k:
        stdout.write("0\n")
      else:
        stdout.write("{}\n".format(nums[v][k-1]))

  except(EOFError):
    break