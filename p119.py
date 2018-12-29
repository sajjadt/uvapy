test_no = 0
while True:
  try:
    num_people = int(input())
    
    people = {x:0 for x in map(str, input().split())}
    for i in range(num_people):
      gift = input().split()
      gifter = str(gift[0])
      amount = int(gift[1])
      num_rec = int(gift[2])

      if amount > 0 and num_rec > 0:
        people[gifter] = people[gifter] - amount +  amount % num_rec
        for person in gift[3:]:
          people[person] = people[person] + amount // num_rec

    if test_no > 0:
      print()
    for people, gain in people.items():
      print("{} {}".format(people, gain))
    
    test_no += 1
  except EOFError:
    break