from heapq import heapify, heappop, heappush

heap = []
while True:
  line = input()

  if line == "#":
    break

  line = line.split()
  
  # Period, job_id, original period (used for generating futur events)
  heap.append((int(line[2]), int(line[1]), int(line[2])))
  heapify(heap)

K = int(input())
for i in range(K):
  v = heappop(heap)
  print(v[1])
  heappush(heap, (v[0] + v[2], v[1], v[2]))
