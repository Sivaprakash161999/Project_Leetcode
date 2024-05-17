from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # post-order traversal - O(n) time; O(n) space
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                if node.val == target:
                    return None
                return node
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right:
                if node.val == target:
                    return None
            return node
        return dfs(root)

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root