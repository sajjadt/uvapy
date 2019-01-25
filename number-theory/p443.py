N = 5842
import heapq
from time import time


start = time()
h = [1]
s = set(h)

heapq.heapify(h)
humble_numbers = [0]
for i in range(N):
  m = heapq.heappop(h)
  s.remove(m)
  humble_numbers.append(m)
  if not m*2 in s:
    s.add(m*2)
    heapq.heappush(h, m*2)
  if not m*3 in s:
    s.add(m*3)
    heapq.heappush(h, m*3)
  if not m*5 in s:
    s.add(m*5)
    heapq.heappush(h, m*5)
  if not m*7 in s:
    s.add(m*7)
    heapq.heappush(h, m*7)

end = time()
# print(end-start)
while True:
  n = int(input())
  if n == 0: break
  if 10 <= (n % 100) < 20:
    suffix = "th"
  elif n % 10 == 1:
    suffix = "st"
  elif n % 10 == 2:
    suffix = "nd"
  elif n % 10 == 3:
    suffix = "rd"
  else:
    suffix = "th"
  print("The {}{} humble number is {}.".format(n, suffix, humble_numbers[n]))
