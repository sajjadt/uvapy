from math import sqrt, pow

def distance_l2(p1, p2):
  return pow(p2[0]-p1[0], 2) + pow(p2[1] - p1[1], 2)


while True:
  try:
    line = input().split()
    n = int(line[0])
    pg = (float(line[1]), float(line[2]))
    pd = (float(line[3]), float(line[4]))

    gopher_scapes = False
    p_scape = None
    for i in range(n):
      line = input().split()
      if gopher_scapes:
        continue

      ph = (float(line[0]), float(line[1]))
      if 4 * distance_l2(ph, pg) <= distance_l2(ph, pd):
        gopher_scapes = True
        p_scape = ph

    if gopher_scapes:
      print("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(p_scape[0], p_scape[1]))
    else:
      print("The gopher cannot escape.")
    input()
  except(EOFError):
    break
    
