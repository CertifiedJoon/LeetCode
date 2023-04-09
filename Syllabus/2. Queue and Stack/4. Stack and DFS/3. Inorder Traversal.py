def inorderTraversal(root):
  while root:
    if (root.left):
      prev = root.left
      while prev.right and prev.right != root:
        prev = prev.right
      if prev.right == None:
        prev.right = root
        root = root.left
      else:
        prev.right = None
        visit(root)
        root = root.right
    else:
      visit(root)
      root = root.right

def visit(node):
  print(node.val)