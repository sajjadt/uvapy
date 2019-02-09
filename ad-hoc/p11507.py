

next_state = {
  '+x' : {'+y':'+y', '-y':'-y', '+z':'+z', '-z':'-z'},
  '-x' : {'+y':'-y', '-y':'+y', '+z':'-z', '-z':'+z'},
  '+y' : {'+y':'-x', '-y':'+x', '+z':'+y', '-z':'+y'},
  '-y' : {'+y':'+x', '-y':'-x', '+z':'-y', '-z':'-y'},
  '+z' : {'+y':'+z', '-y':'+z', '+z':'-x', '-z':'+x'},
  '-z' : {'+y':'-z', '-y':'-z', '+z':'+x', '-z':'-x'}
}

from sys import stdin, stdout
while True:
  l = int(input())
  if l == 0:
    break

  bends = input().split()
  
  state = '+x'
  for b in bends:
    if b == 'No':
      continue
    else:
      state = next_state[state][b]

  print(state)