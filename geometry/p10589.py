from math import sqrt, pow

def distance(p_a, p_b):
  return sqrt(pow(p_b[0]-p_a[0], 2) + pow(p_b[1] - p_a[1], 2))

while True:
  n, a = list(map(int, input().split()))
  if n == a == 0:
    break
  
  p_a = (0, 0)
  p_b = (a, 0)
  p_c = (a, a)
  p_d = (0, a)
  m = 0

  for i in range(n):
    p = tuple(map(float, input().split()))
    
    # this point is within the center area of its distance to corners is less than a
    if distance(p, p_a) < a and \
      distance(p, p_b) < a and \
      distance(p, p_c) < a and \
      distance(p, p_d) < a:
      m += 1
  
  print("{:.5f}".format((a*a) * (m/n)))
    


