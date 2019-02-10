from sys import stdin, stdout
from enum import Enum
from functools import cmp_to_key

PARTI_LIMIT = 101
PROBLEM_LIMIT = 11


class Submission(Enum):
  CORRECT = 0
  INCORRECT = 1
  OTHER = 2

class Participant:
  def __init__(self, id):
    self.id = id
    self.solved = set([])
    self.penalty = 0
    self.accum_penalty = [0]*PROBLEM_LIMIT
  
  def submit(self, problem, time, verdict):

    if verdict == Submission.CORRECT:
      if not problem in self.solved:
        self.solved.add(problem)
        self.penalty += time
        self.penalty += self.accum_penalty[problem]

    elif verdict == Submission.INCORRECT:
      if not problem in self.solved:
        self.accum_penalty[problem] += 20

# Sort function
def sorted_by(a, b):
  if len(a.solved) == len(b.solved):
    if a.penalty == b.penalty:
      return b.id - a.id
    else:
      return b.penalty - a.penalty
  else:
    return len(a.solved) - len(b.solved)

cmp_function = cmp_to_key(sorted_by)


cases = int(stdin.readline())
stdin.readline()


for c in range(cases):
  submissions = []
  participants = {}
  submission_order = []

  line = stdin.readline().strip()
  while line != "":
    team, problem, time, verdict = line.split()
    line = stdin.readline().strip()

    team = int(team)
    problem = int(problem)
    time = int(time)

    if not team in participants:
      participants[team] = Participant(team)
    
    participants[team].submit(problem, time, Submission.CORRECT if verdict == "C" else Submission.INCORRECT if verdict == "I" else Submission.OTHER)

  if c > 0:
    print()

  participants = list(participants.values())
  participants.sort(key=cmp_function, reverse=True)
  for team in participants:
    print("{} {} {}".format(team.id, len(team.solved), team.penalty))