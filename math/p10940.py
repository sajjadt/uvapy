
def f(n):
  if n <= 2:
    return n
  if n % 2 == 0:
    # With even number of cards, there will be a new deck f([2, 4, 6, n]) or 2*f([1,2,3, n//2])
    return 2*f(n//2)
  else:
    # With odd number of cards, there will be a new deck f([n, 2, 4, n-1]) or 2*(f([0+1, 1+1, 2+1, 3+1, n//2+1])-1)
    return 2*(f(n//2 + 1)-1)


from sys import stdin, stdout
while True:
  n = int(stdin.readline().strip())
  if n == 0:
    break
  
  stdout.write("{}\n".format(f(n)))
