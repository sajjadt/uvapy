import operator

def to_min(time):
  time = time.split(":")
  return int(time[0])*60 + int(time[1])

def to_date(mins):
  hrs, mins = divmod(mins, 60)
  if hrs > 0:
    return "{} hours and {} minutes".format(hrs, mins)
  else:
    return "{} minutes".format(mins)


day = 1
while True:
  try:
    n = int(input())
    
    events = [[600,600,"10:00"], [1080, 1080,"18:00"]]

    for i in range(n):
      line = input().strip().split()
      start = line[0]
      end = line[1]
      events.append([to_min(start), to_min(end), end])
    
    
    events.sort()
    gaps = [events[i+1][0] - events[i][1] for i in range(len(events)-1)]
    max_id, max_val = max(enumerate(gaps), key=operator.itemgetter(1))

    print("Day #{}: the longest nap starts at {} and will last for {}.".format(day, events[max_id][2], to_date(max_val))) 
    day +=1

  except(EOFError):
    break