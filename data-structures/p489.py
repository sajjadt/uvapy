while True:
  case = int(input())
  
  if case == -1:
    break
  
  sol = set(input())
  guess = input()

  num_wrong_guesses = 0
  num_unique_letters = len(sol)
  num_right_guesses = 0
  guessed_before = set([])
  
  win = lose = False
  for ch in guess:
    if ch in guessed_before:
      continue
    
    guessed_before.add(ch)

    if ch in sol:
      num_right_guesses += 1
      if num_right_guesses == num_unique_letters:
        win = True
        break  
    else:
      num_wrong_guesses += 1
      if num_wrong_guesses == 7:
        lose = True
        break 
  
  print("Round {}".format(case))
  if win:
    print("You win.")
  elif lose:
    print("You lose.")
  else:
    print("You chickened out.")


