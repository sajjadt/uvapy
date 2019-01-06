num_tests = int(input())


for test in range(num_tests):
  diff = 0
  num_tracks = 0

  tracks = list(map(str, input().split()))
  for track in tracks:
    if track == "MM":
      diff += 1
    elif track == "FF":
      diff -= 1
    num_tracks += 1
  
  print("LOOP" if diff == 0 and num_tracks > 1 else "NO LOOP")
