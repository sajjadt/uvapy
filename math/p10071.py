
while True:
  try:
    v, t = list(map(int, input().split()))
    print(v * t * 2)    
  except EOFError:
    break
