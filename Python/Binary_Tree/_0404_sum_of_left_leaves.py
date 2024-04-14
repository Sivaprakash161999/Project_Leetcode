from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs - recursive - O(n) time; O(n) space
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, type):
            if not node:
                return 0
            if not node.left and not node.right:
                if type == 'l':
                    return node.val
                else:
                    return 0
            return dfs(node.left, 'l') + dfs(node.right, 'r')
        return dfs(root, 'root')

    # dfs - iterative - O(n) time; O(n) space
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        stack = [(root, 'root')]
        while stack:
            node, kind = stack.pop()
            if not node.left and not node.right and kind == 'l':
                ans += node.val
            if node.left:
                stack.append((node.left, 'l'))
            if node.right:
                stack.append((node.right, 'r'))
        return ans

    # bfs - queue - O(n) time; O(n) space
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        ans = 0
        queue = deque([(root, False)])
        while queue:
            node, isLeft = queue.popleft()
            if not node.left and not node.right and isLeft:
                ans += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        return ans 

        