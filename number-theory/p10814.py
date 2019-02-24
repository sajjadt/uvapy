from fractions import Fraction
from sys import stdin, stdout

def gcd(a, b):
  while(b): 
    a, b = b, a % b 
  return a


cases = int(stdin.readline().strip())
for c in range(cases):
  line = stdin.readline().strip().split("/")
  a = int(line[0].strip())
  b = int(line[1].strip())
  
  # Using Fraction
  # fraction = Fraction(a, b)
  # stdout.write("{} / {}\n".format(fraction.numerator, fraction.denominator))

  # Own implemention
  c = gcd(a, b)
  stdout.write("{} / {}\n".format(a//c, b//c))
