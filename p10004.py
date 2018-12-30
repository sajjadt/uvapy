while True:
  try:
    num_v = int(input())
    num_e = int(input())
    
    e = {i: [] for i in range(num_v)}

    for i in range(num_e):
      line = input().split()
      src, dst = int(line[0]), int(line[1])
      e[src].append(dst)
      e[dst].append(src)

    seen = {} # v_id: int: is_0_colored: boolean
    
    bicolorable = True
    v_id = 0
    v_processor = [(0, True)]

    while v_id < len(v_processor):
      p = v_processor[v_id]
      seen[p[0]] = p[1]

      for dst in e[p[0]]:
        if dst in seen:
          if p[1] == seen[dst]:
            bicolorable = False
            break
        else: 
          v_processor.append((dst, not p[1]))
  
      v_id += 1

      if not bicolorable:
        break

    if bicolorable:
      print("BICOLORABLE.")
    else:
      print("NOT BICOLORABLE.")
  except(EOFError):
    break
