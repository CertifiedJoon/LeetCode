# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        large = max(p.val, q.val)
        small = min(p.val, q.val)
        while root:
            if root.val >= small and root.val <= large:
                return root
            elif root.val > large:
                root = root.left
            else:
                root = root.right
        raise Exception