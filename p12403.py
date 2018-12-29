num_cmds = int(input())
funds = 0
for i in range(num_cmds):
  cmd = str(input()).split()
  if len(cmd) == 1:
    print(funds)
  else:
    funds += int(cmd[1])