# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if k == 0:
                return node.val
            node = stack.pop()
            root = node.right
            k -= 1
