#!/usr/bin/python3

def fib(n):
  return pow(2 << n, n + 1, (4 << 2*n) - (2 << n) - 1) % (2 << n)

while True:
  try:
    n = int(input())
    print(fib(n))
  except EOFError:
    break

