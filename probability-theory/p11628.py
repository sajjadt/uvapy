from fractions import Fraction
from sys import stdin, stdout


while True:
  n, m = list(map(int, stdin.readline().strip().split()))

  if n == m == 0:
    break

  last_round_tickets = []
  for i in range(n):
    line = stdin.readline().strip()
    ticket = int(line[line.rfind(" ")+1:])
    last_round_tickets.append(ticket)

  total = sum(last_round_tickets)
  for ticket in last_round_tickets:
    frac = Fraction(ticket, total)
    stdout.write("{} / {}\n".format(frac.numerator, frac.denominator))
