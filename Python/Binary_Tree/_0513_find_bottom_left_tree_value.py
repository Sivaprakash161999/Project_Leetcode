from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # dfs
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = -1
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        return self.bottomLeftValue

    def dfs(self, current: TreeNode, depth: int):
        if not current:
            return
        
        if depth > self.maxDepth:  # If true, we discovered a new level
            self.maxDepth = depth
            self.bottomLeftValue = current.val

        self.dfs(current.left, depth + 1)
        self.dfs(current.right, depth + 1)
        return

    # bfs - level order
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val

        