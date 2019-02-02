class Cube:
  def __init__(self, xl=0, xr=0, yl=0, yr=0, zl=0, zr=0):
    self.xl = xl
    self.xr = xr
    self.yl = yl
    self.yr = yr
    self.zl = zl
    self.zr = zr

  def volume(self):
    return (self.xr-self.xl) * (self.yr-self.yl) * (self.zr-self.zl)


def intersect(cube1, cube2):
  if cube2.xl >= cube1.xr or cube2.yl >= cube1.yr or cube2.zl >= cube1.zr \
    or cube1.xl >= cube2.xr or cube1.yl >= cube2.yr or cube1.zl >= cube2.zr:
    return Cube()

  c1 = cube1
  c2 = cube2
  cube = Cube(max(c1.xl, c2.xl), min(c1.xr, c2.xr), 
              max(c1.yl, c2.yl), min(c1.yr, c2.yr), 
              max(c1.zl, c2.zl), min(c1.zr, c2.zr))
  return cube

while True:
  n = int(input())
  if n == 0:
    break
  
  x, y, z, side = list(map(int, input().split()))
  cube = Cube(x, x+side, y, y+side, z, z+side)
  # print(cube.volume())
  for i in range(1, n):
    
    x, y, z, side = list(map(int, input().split()))
    if cube.volume() == 0:
      continue
    temp_cube = Cube(x, x+side, y, y+side, z, z+side)
    # print(temp_cube.volume())
    cube = intersect(temp_cube, cube)

  print(cube.volume())