def build_tree_map(root, answer):
  if not root:
    return 
  new_map = dict()
  left = build_tree_map(root.left)
  right = build_tree_map(root.right)
  if left == right:
    answer.append(left.key)
  new_map[root.val]=(left, right)
  return new_map

from collections import defaultdict

class Solution:
  def findDuplicateSubtrees(self, root):
    def traverse(node):
      if not node:
        return 0
      triplet = (traverse(node.left), node.val, traverse(node.right))
      if triplet not in triplet_to_id:
        triplet_to_id[triplet] = len(triplet_to_id) + 1
      id = triplet_to_id[triplet]
      cnt[id] += 1
      if cnt[id] == 2:
        res.append(node)
      return id

    triplet_to_id = dict()
    cnt = defaultdict(int)
    res = []
    traverse(root)
    return res
