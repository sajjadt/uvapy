import functools

class Team:
  def __init__(self, name):
    self.name = name
    self.games_played = 0
    self.goals_scored = 0
    self.goals_received = 0
    self.points = 0
    self.wins = 0
    self.losses = 0
    self.ties = 0

  def apply_game(self, scored, received):
    self.games_played += 1
    self.goals_received += received
    self.goals_scored += scored
    self.points += (1 if scored == received else 3 if scored > received else 0)
    self.wins += (1 if scored > received else 0)
    self.losses += (1 if scored < received else 0)
    self.ties += (1 if scored == received else 0)

  def __str__(self):
    return "{} {}p, {}g ({}-{}-{}), {}gd ({}-{})".format(self.name, self.points, self.games_played, \
      self.wins, self.ties, self.losses, self.goals_scored-self.goals_received, self.goals_scored, self.goals_received)

def cmp_str(a, b):
  for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
      continue
    if a[i].islower() == b[i].islower():
      return ord(b[i]) - ord(a[i])
    else:
      if a[i].islower():
        return 1
      else:
        return -1
        
# Negative for less than, positive for higher, zero for equal
def sorted_by(t1, t2):
  if t1.points == t2.points:
    if t1.wins == t2.wins:
      if (t1.goals_scored - t1.goals_received) == (t2.goals_scored - t2.goals_received):
        if t1.goals_scored == t2.goals_scored:
          if t1.games_played == t2.games_played:
            return cmp_str(t1.name.lower(), t2.name.lower())
          else:
            return t2.games_played - t1.games_played
        else:
          return t1.goals_scored - t2.goals_scored
      else:
        return (t1.goals_scored - t1.goals_received) - (t2.goals_scored - t2.goals_received)
    else:
      return t1.wins - t2.wins
  else:
    return t1.points - t2.points

cmp_function = functools.cmp_to_key(sorted_by)


num_cups = int(input())

for c in range(num_cups):
  tour = input()
  num_teamns = int(input())

  teams = {}
  for i in range(num_teamns):
    name = input().strip()
    teams[name] = Team(name)

  num_matches = int(input())
  for i in range(num_matches):
    match = input().strip()
    info = match.split("#")
    t1 = teams[info[0].strip()]
    t2 = teams[info[2].strip()]
    gl, gh = list(map(int, info[1].strip().split("@")))
    t1.apply_game(gl, gh)
    t2.apply_game(gh, gl)

  t = list(teams.values())
  t.sort(key = cmp_function, reverse=True)

  if c > 0:
    print()
  print(tour)
  for i in range(len(t)):
    print("{}) {}".format(i+1, str(t[i])))
  