
def visit(in_order_t, start):

  leaves_acc= {}
  # Process in_order traversal text as we visit
  def __visit(index, level):
    ''' Return last processed index of in_order_t'''
    if in_order_t[index] == -1:
      return index
    
    v = in_order_t[index]
    if level in leaves_acc:
      leaves_acc[level] += v
    else:
      leaves_acc[level] = v

    new_index = __visit(index+1, level-1)
    return __visit(new_index+1, level+1)

  last_processed = __visit(start, 0)

  return last_processed, [p[1] for p in sorted(leaves_acc.items())]


# Read all the input
import sys
in_order_t = []
for line in sys.stdin:
  in_order_t += list(map(int, line.strip().split()))


last_processed = -1
case = 1

while last_processed + 2 < len(in_order_t): 
  last_processed, res = visit(in_order_t, last_processed + 1)
  sys.stdout.write("Case {}:\n{}\n\n".format(case, " ".join(map(str, res))))
  case += 1