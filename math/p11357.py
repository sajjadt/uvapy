# Special case of SAT
# It is enough to check if one clause can be satisifed

def check_clause(clause):
  v_set = set([])
  inv_set = set([])
  vars = clause[1:-1].split("&")
  for var in vars:
    if var[0] == "~":
      if var[1] in v_set:
        return False
      inv_set.add(var[1]) 
    else:
      if var in inv_set:
        return False
      v_set.add(var)  
  return True

from sys import stdin, stdout

cases = int(stdin.readline().strip())
for i in range(cases):
  formula = stdin.readline().strip()
  clauses = formula.split("|")
  if any(check_clause(c) for c in clauses):
    stdout.write("YES\n")
  else:
    stdout.write("NO\n")