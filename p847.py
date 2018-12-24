from math import ceil

if __name__ == '__main__':
  while True:
    try:
      n = int(input())
      
      start_ = 1
      end_ = 1
      ollie_wins = True

      while (end_ < n):
        if ollie_wins:
          start_ = end_ + 1
          end_ = end_ * 9
        else:
          start_ = end_ + 1
          end_ = end_ * 2
        ollie_wins = not ollie_wins

      if ollie_wins:
        print("Ollie wins.")
      else:
        print("Stan wins.")

    except(EOFError):
      break
  