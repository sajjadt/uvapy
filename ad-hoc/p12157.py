from math import ceil
num_tests = int(input())

for t in range(num_tests):
  input()
  cases = list(map(int, input().split()))
  mile = sum(map(lambda x: ceil((x+1)/30)*10, cases))
  juice = sum(map(lambda x: ceil((x+1)/60)*15, cases))
  if mile < juice:
    print("Case {}: Mile {}".format(t+1, mile))
  elif juice < mile:
    print("Case {}: Juice {}".format(t+1, juice))
  else:
    print("Case {}: Mile Juice {}".format(t+1, juice))

