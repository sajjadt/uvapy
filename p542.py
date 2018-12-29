
sol_space = {}
def foo(team_i, start, end):
  global teams
  global p_win
  global sol_space

  assert team_i >= start and team_i < end

  num_teams = end - start
  if num_teams == 1:
    return 1

  if (team_i, start, end) in sol_space:
    return sol_space[(team_i, start, end)]

  psum = 0
  # team_i becomes champion of eitehr start:start+x or start+x:end
  if team_i >= start + num_teams // 2:
    result = foo(team_i, start + num_teams // 2, end)
    for i in range(start, start + num_teams // 2):
      psum += foo(i, start, start + num_teams // 2) * p_win[team_i][i] * 0.01
    result *= psum
  else :
    result = foo(team_i, start, start + num_teams // 2)
    for i in range(start + num_teams // 2, end):
      psum += foo(i, start + num_teams // 2, end) * p_win[team_i][i] * 0.01
    result *= psum
  
  sol_space[(team_i, start, end)] = result
  return result

teams = []
for i in range(16):
  teams.append(str(input()))

p_win = []
for i in range(16):
  p = list(map(int, input().split()))
  p_win.append(p)

p_all = [foo(i, 0, 16) for i in range(16)]

for team, p in zip(teams, p_all):
  print("{0:10} p={1:.2f}%".format(str(team), p*100))



