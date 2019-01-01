class Node:
  def __init__(self, left=None, right=None, has_value=False):
    self.left = left
    self.right = right
    self.has_value = has_value

def add_code(g, code):
  current = g
  success = True

  for ch in code:
    if ch == "0":
      if not current.left:
        current.left = Node()
      current = current.left

    else:
      if not current.right:
        current.right = Node()
      current = current.right
    
    if current.has_value:
      success = False
      break
  current.has_value = True

  return success

set_no = 1
root = Node()
inputs = []
while True:
  try:
    code = str(input())

    if code == "9":
      inputs = sorted(inputs)
      # print(inputs)
      decodable = True

      for code in inputs:
        decodable = add_code(root, code)
        if not decodable:
          break
      
      print("Set {} is {}immediately decodable".format(str(set_no), "" if decodable else "not "))
      root = Node()
      set_no += 1
      inputs.clear()

    else:
      inputs.append(code)
      


  except(EOFError):
    break
  
  