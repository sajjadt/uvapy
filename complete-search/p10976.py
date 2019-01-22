
# 1/k = 1/x + 1/y and k, x, y > 0
# In a valid solution, k > x and k > y
# x >= y to count only for one of the symmetric solutions

from sys import stdout
while True:
  try:
    k = int(input())

    x = k + 1
    y = (x*k) // (x - k)
    sols = []
    while y > k and y >= x:    
      y, r = divmod(x*k, x - k)
      if r == 0:
        sols.append([x, y])
      x += 1
    
    stdout.write("{}\n".format(len(sols)))
    stdout.write("\n".join(["1/{} = 1/{} + 1/{}".format(k, y, x) for x,y in sols]))
    stdout.write("\n")

  except(EOFError):
    break
