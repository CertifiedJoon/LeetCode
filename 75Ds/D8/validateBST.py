# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        prev = None
        last_seen = float('-inf')
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left
                elif prev.right == root:
                    prev.right = None
                    if root.val <= last_seen:
                        return False
                    else:
                        last_seen = root.val
                    root = root.right
            else:
                if last_seen >= root.val:
                    return False
                else:
                    last_seen = root.val
                root = root.right
        return True