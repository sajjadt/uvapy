
# Asuume at year y, bit_width equals to b
# Number of unsigned number that can be represented equals to 2^b
# We are looking for largest k such that k! < 2^(b)
# It is expensive to calcuate both these quenatities given the input size
# k! < 2^(b) ->
# log2 k! < b 
# log2 1 + log2 2 + ... + log2 k < b

from time import time
from sys import stdin, stdout

# Code to caclucate solution
# from math import log2
# sol = {}
# t1 = time()
# bit_width = 2
# for i in range(21):
#   bit_width *= 2
#   year = 1960+i*10
#   val = 0
#   k = 2
#   while val < bit_width:
#     val += log2(k)
#     k += 1 
#   sol[year//10] = k-2
# t2 = time()
# print(t2 - t1)

sol = {
  196: 3, 197: 5, 198: 8, 199: 12, 200: 20, 201: 34, 202: 57, 
  203: 98, 204: 170, 205: 300, 206: 536, 207: 966, 208: 1754, 
  209: 3210, 210: 5910, 211: 10944, 212: 20366, 213: 38064, 
  214: 71421, 215: 134480, 216: 254016
}

while True:
  n = int(stdin.readline().strip())
  if n == 0:
    break
  stdout.write("{}\n".format(sol[n//10]))