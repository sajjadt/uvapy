from sys import stdin, stdout

num_cases = int(stdin.readline().strip())
for t in range(num_cases):
  n = int(stdin.readline().strip())

  # Sol = sum ( k * c(n, k)) for k in [1, n] 
  # which is equal to sum (n * c(n-1, k-1)) for k in [1, n]
  # Referring to Pascal's triangle: sum (c(n-1, k-1)) == 2**n-1
  # sol = n * pow (2, n-1)

  # sol must be reported modulo 1000000007
  # Python to the rescue
  # Otherwise we should do log(n) steps
  sol = n * pow (2, n-1, 1000000007) % 1000000007

  stdout.write("Case #{}: {}\n".format(t+1, sol))
