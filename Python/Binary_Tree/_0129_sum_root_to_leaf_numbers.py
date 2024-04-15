from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs - O(n) time; O(n) space
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            nonlocal root_to_leaf_sum
            if not node:
                return 0
            if not node.left and not node.right:
                root_to_leaf_sum += num*10 + node.val
            if node.left:
                dfs(node.left, num*10 + node.val)
            if node.right:
                dfs(node.right, num*10 + node.val)

        root_to_leaf_sum = 0
        dfs(root, 0)
        return root_to_leaf_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node:
                return 0
            if not node.left and not node.right:
                return num*10 + node.val
            return (dfs(node.left, num*10 + node.val)
                    + dfs(node.right, num*10 + node.val))
        return dfs(root, 0)

    # dfs - stack
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0)]
        while stack:
            node, num = stack.pop()
            if not node:
                res += 0
            if not node.left and not node.right:
                res += num*10 + node.val
            if node.left:
                stack.append((node.left, num*10 + node.val))
            if node.right:
                stack.append((node.right, num*10 + node.val))
        return res

    # bfs - queue
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([(root, 0)])
        while queue:
            node, num = queue.popleft()
            if not node:
                res += 0
            if not node.left and not node.right:
                res += num*10 + node.val
            if node.left:
                queue.append((node.left, num*10 + node.val))
            if node.right:
                queue.append((node.right, num*10 + node.val))
        return res