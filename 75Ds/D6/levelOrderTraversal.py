# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = deque()
        level = 0
        q.append((root, level))
        traversed = []
        while q:
            parent, level = q.popleft()
            if level > len(traversed) - 1:
                traversed.append([parent.val,])
            else:
                traversed[level].append(parent.val)
            if parent.left:
                q.append((parent.left, level + 1))
            if parent.right:
                q.append((parent.right, level + 1))
        return traversed
            