from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs recursive - O(n) time; O(n) space
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        def dfs(node, deep):
            if not node:
                return
            if deep == depth - 1:
                tmp_left, tmp_right = node.left, node.right
                node.left = TreeNode(val, tmp_left)
                node.right = TreeNode(val, None, tmp_right)
                return
            dfs(node.left, deep + 1)
            dfs(node.right, deep + 1)
        dfs(root, 1)
        return root

    # dfs iterative - O(n) time; O(n) space
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        stack = [(root, 1)]
        while stack:
            node, deep = stack.pop()
            if deep == depth - 1:
                tmp_left, tmp_right = node.left, node.right
                node.left = TreeNode(val, tmp_left)
                node.right = TreeNode(val, None, tmp_right)
            if node.left:
                stack.append((node.left, deep + 1))
            if node.right:
                stack.append((node.right, deep + 1))
        return root

    # bfs queue - O(n) time; O(n) space
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        queue = deque([root])
        for i in range(2, depth):
            for j in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        for i in range(len(queue)):
            node = queue.popleft()
            tmp_left, tmp_right = node.left, node.right
            node.left = TreeNode(val, tmp_left)
            node.right = TreeNode(val, None, tmp_right)
        return root

        