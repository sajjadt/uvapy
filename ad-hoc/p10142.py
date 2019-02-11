from sys import stdin, stdout

num_cases = int(stdin.readline())
stdin.readline()

for case in range(num_cases):

  n = int(stdin.readline().strip())  # num_candidates
  candidates = []
  for i in range(n):
    candidates.append(stdin.readline().strip())
  
  votes = []
  
  line = stdin.readline().strip()
  while line != "":
    votes.append(list(map(lambda x: int(x) - 1, line.split())))
    line = stdin.readline().strip()

  # This set keeps track of candidates that are eliminated in vote counting cycle
  eliminated = set([])
  v = len(votes)
  
  pointers = [0] * v
  is_decided = False

  if case > 0:
    stdout.write("\n")

  while not is_decided:

    # Re-count the votes
    total_votes = [0]*n
    for i in range(v):
      # advance pointers[i] till it points to a candidate still in the race
      p = pointers[i]
      while votes[i][p] in eliminated:
        p += 1
      pointers[i] = p
      # Pointers[i] point to a valid vote
      total_votes[votes[i][p]] += 1
    
    # Find max vote (no need to check if not eliminated)
    max_vote = max(total_votes)
    # Check if it is more than 50 percents
    if max_vote*2 >= v :
      is_decided = True
      for iv in range(len(total_votes)):
        if total_votes[iv] == max_vote:
          stdout.write(candidates[iv] + "\n")
    else:
      min_vote = -1
      for vi, vv in enumerate(total_votes):
        if not vi in eliminated:
          if min_vote == -1:
            min_vote = vv
          else:
            min_vote = min(vv, min_vote)
      # make sure min is not already eliminated
      if min_vote == max_vote:
        # No one left to eliminate
        is_decided = True
        for i, guy in enumerate(candidates):
          if not i in eliminated:
            stdout.write(guy + "\n")
      else:
        # find everyone with min_vote and eliminate them
        for k in range(n):
          if total_votes[k] == min_vote:
            eliminated.add(k)
  


  