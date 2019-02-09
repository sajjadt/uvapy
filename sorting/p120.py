while True:
  try:
    unsorted_set = list(map(int, input().split()))
    working_set = unsorted_set.copy()
    sorted_set = sorted(unsorted_set)

    N = len(sorted_set)
    steps_to_sort = []
    for i in range(len(working_set)-1, -1, -1):
      # Check if ith element is sorted, sort it if not.
      index  = working_set.index(sorted_set[i])
      if index == i:
        continue

      if index == 0:
        # One Flip
        working_set[0:i+1] = working_set[0:i+1][::-1]
        steps_to_sort.append(N - i)
      else:
        # Two flips
        working_set[0:index+1] = working_set[0:index+1][::-1]
        working_set[0:i+1] = working_set[0:i+1][::-1]

        steps_to_sort.append(N - index)
        steps_to_sort.append(N - i)

    steps_to_sort.append(0)
    print(" ".join(map(str, unsorted_set)))
    print(" ".join(map(str, steps_to_sort)))

  except(EOFError):
    break