def deepcopy(node):
  q = deque
  q.append(node)
  copied = {1: Node(node.val)}
  while q:
    curr = q.popleft()
    for nb in curr.neighbors:
      if nb.val not in copied:
        copied[nb.val] = Node(nb.val)
        q.append(nb)
      copied[curr.val].neighbors.append(copied[nb.val])