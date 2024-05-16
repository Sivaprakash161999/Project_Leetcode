from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    # post order - O(n) time; O(n) space
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left:
                return node.val == 1
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) and dfs(node.right)
        return dfs(root)
        
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val == 1
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        return (left or right) if root.val == 2 else (left and right)