"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        traversed = []
        #Iterative method
        if not root:
            return []
        stack = [root,]
        while stack:
            parent = stack.pop()
            traversed.append(parent.val)
            stack.extend(parent.children[::-1])

        #Recursive method
        #self.rec_preorder(root, traversed)
        return traversed

    def rec_preorder(self, root, traversed):
        if not root:
            return
        traversed.append(root.val)
        for child in root.children:
            self.rec_preorder(child, traversed)
        return

                
