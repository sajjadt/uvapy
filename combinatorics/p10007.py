
# f(n) = n! "to permute the n numbers, then the first one 
# can be selected as root" * sum(f(i)*f(n-1-i) for i in range[0, n-1])
# => f(n) = n!*C(n) C(n) is nth number in catalan sequence

LIMIT = 300 + 1
catalan = [1, 1]
results = [1]
fact = 1

for i in range(1, LIMIT):
  catalan.append(((4*i+2) * catalan[i])//(i+2))
  fact *= i
  results.append(fact*catalan[i])

while True:
  n = int(input())
  if n == 0:
    break
  
  print(results[n])