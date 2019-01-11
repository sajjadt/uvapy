num_cases = int(input())

for t in range(num_cases):  
  f, s = list(map(str, input().split("-")))

  f_val = sum([(ord(d) - ord("A"))*pow(26, i) for i,d in enumerate(reversed(f))])  
  s_val = int(s)

  if abs(f_val - s_val) <= 100:
    print("nice")
  else:
    print("not nice")
