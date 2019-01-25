def post_order(pre_t, in_t):
  ''' pre_t and in_t contains letters from a-z A-Z with no duplication'''
  # assert len(pre_t) == len(in_t)
  if len (pre_t) == 0:
    return ""
  if len(pre_t) == 1:
    return pre_t
  ind = in_t.index(pre_t[0])
  return post_order(pre_t[1:1+ind], in_t[0:ind]) + post_order(pre_t[ind+1:], in_t[ind+1:]) + pre_t[0]

num_cases = int(input())

for t in range(num_cases):
  line = input().split()
  pre_order_t = str(line[1])
  in_order_t = str(line[2])
  print(post_order(pre_order_t, in_order_t))
