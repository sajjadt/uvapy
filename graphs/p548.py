
class Node:
  def __init__(self, value=-1):
    self.value = value
    self.right = None
    self.left = None
    self.min_path_val = 0
    self.min_leaf_val = 0


def create_tree(in_t, post_t):
  # assert len(in_t) == len(post_t)

  if len(in_t) == 1:
    return Node(in_t[0])
  root = Node()
  i = in_t.index(post_t[-1])
  root.left = create_tree(in_t[:i], post_t[:i]) if i > 0 else None
  root.right = create_tree(in_t[i+1:], post_t[i:-1]) if i < len(in_t) - 1 else None
  root.value = post_t[-1]
  return root

def calc_min_leaf_val(root):
  if root == None:
    return None, None
  else:

    left_v, left_l = calc_min_leaf_val(root.right)
    right_v, right_l = calc_min_leaf_val(root.left)

    if left_v != None and right_v != None:
      if left_v < right_v:
        root.min_path_val = root.value +  left_v
        root.min_leaf_val = left_l
      else:
        root.min_path_val = root.value +  right_v
        root.min_leaf_val = right_l
    elif left_l != None:
      root.min_path_val = root.value +  left_v
      root.min_leaf_val = left_l
    elif right_l != None:
      root.min_path_val = root.value +  right_v
      root.min_leaf_val = right_l
    else:
      root.min_path_val = root.value
      root.min_leaf_val = root.value
    return root.min_path_val, root.min_leaf_val


from sys import stdin, stdout
while True:
  try:
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    root = create_tree(in_order, post_order)
    print(calc_min_leaf_val(root)[1])
  except(EOFError):
    break