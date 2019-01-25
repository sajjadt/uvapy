import re
from sys import stdin

class Node:
  def __init__(self):
    self.left = None
    self.right = None
    self.has_value = False
    self.value = None

def tree_from_s_expr(source):
  number_or_symbol = re.compile('(-*\d+|[^ 0-9\n])')
  root = None
  target = None
  nodes = []
  tokens = re.findall(number_or_symbol, source)
  for token in tokens:
    if token == "(":
      n = Node()
      if len(nodes) > 0:
        if nodes[-1].left == None: 
          nodes[-1].left = n
        else:
          nodes[-1].right = n
      else:
        root = n
      nodes.append(n)
    elif token == ")":
      nodes.pop()
      if len(nodes) == 0:
        yield target, root
        root = None
        target = None
    else:
      if len(nodes) == 0:
        target = int(token)
      else:
        nodes[-1].value = int(token)
        nodes[-1].has_value = True
  return

def sum_path_exists(root, current, target):
  total = current
  if not root:
    return False
  if root.has_value:
    total += root.value
    
    # if leaf
    if root.left.has_value == root.right.has_value == False:
      return total == target
    
    if sum_path_exists(root.left, total, target):
      return True
    return sum_path_exists(root.right, total, target)
    

inp = "".join([l for l in stdin])
for target, root in tree_from_s_expr(inp):
  print("yes" if sum_path_exists(root, 0, target) else "no")
