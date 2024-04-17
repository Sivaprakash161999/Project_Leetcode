from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs + sorting 
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        strings = []
        def dfs(node, s):
            nonlocal strings
            if not node:
                return
            if not node.left and not node.right:
                strings.append(chr(node.val + ord('a')) + s)
                return
            dfs(node.left, chr(node.val + ord('a')) + s)
            dfs(node.right, chr(node.val + ord('a')) + s)
        dfs(root, '')
        strings.sort()
        return strings[0]
    

    # No need to explicitly sort, since min will take care of smallest string
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        table = [chr(ord('a') + i) for i in range(26)]
        def dfs(node, currStr):
            if not node:
                return currStr
            if not node.left:
                return dfs(node.right, table[node.val] + currStr)
            if not node.right:
                return dfs(node.left, table[node.val] + currStr)
            return min(dfs(node.left, table[node.val] + currStr),
                        dfs(node.right, table[node.val] + currStr))
        return dfs(root, '')
        

    # bfs - O(n**2) time; O(n**2) space
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallestString = 'z' * 30
        queue = deque([(root, '')])
        while queue:
            node, currStr = queue.popleft()
            currStr = chr(node.val + ord('a')) + currStr
            if not node.left and not node.right:
                smallestString = min(smallestString, currStr)
            if node.left:
                queue.append((node.left, currStr))
            if node.right:
                queue.append((node.right, currStr))
        return smallestString