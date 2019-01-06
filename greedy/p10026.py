#!/usr/bin/python3
import functools

def job_cmp(a, b):
  if a[0]*b[1] > b[0]*a[1]:
    return 1
  elif a[0]*b[1] == b[0]*a[1]:
    return 0
  else:
    return -1

num_tests = int(input())


for i in range(num_tests):
  input() # blank line
  num_jobs = int(input())
  jobs = []

  for j in range(num_jobs):
    T, S = [int(x) for x in input().split()]
    jobs.append((T, S, j+1)) 
  jobs = sorted(jobs, key = functools.cmp_to_key(job_cmp), reverse=False)

  if i > 0:
    print()
  print(" ".join([str(j[2]) for j in jobs]))
  

