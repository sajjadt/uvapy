import functools

def sorted_by(a, b):
  if a[0] == b[0]:
    return -1 if a[1].lower() < b[1].lower() else 1 if a[1].lower() > b[1].lower() else 0
  else:
    return a[0] - b[0]
cmp_function = functools.cmp_to_key(sorted_by)


from sys import stdin, stdout
while True:
  try:
    num_racers = int(stdin.readline().strip())

    times = []
    for i in range(num_racers):
      line = stdin.readline().strip()
      racer, time = line.split(":")
      racer = racer.strip()
      time = time.strip().split()
      mins = int(time[0])
      secs = int(time[2])
      milli_secs = int(time[4]) 
      times.append([milli_secs + secs*1000 + mins*60000, racer])
    times.sort(key=cmp_function)


    row = 1
    for i in range(0, len(times)-1, 2):
      stdout.write("Row {}\n{}\n{}\n".format(row, times[i][1], times[i+1][1]))
      row +=1 

    if len(times) & 1 == 1:
      stdout.write("Row {}\n{}\n".format(row, times[-1][1]))

    stdout.write("\n")
    input()
    
  except(EOFError):
    break
