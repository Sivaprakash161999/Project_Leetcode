from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    # recursive - dfs
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))

    # iterative - bfs
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue = deque()
        queue.append([p, q])
        while queue:
            r1, r2 = queue.popleft()
            if r1 and r2: # both are valid nodes
                if r1.val == r2.val: # both nodes have same value
                    queue.append([r1.left, r2.left]) # add the left children of both 
                                                        #nodes to the queue
                    queue.append([r1.right, r2.right]) # add the right children
                else: # nodes have different value
                    return False
            elif r1 or r2: # one of them is node and other is None
                return False
        return True # we have traversed all the nodes, 
    #                 # and all have same values

    # iterative - dfs
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack = []
        stack.append([p, q])
        while stack:
            r1, r2 = stack.pop()
            if r1 and r2: # both are valid nodes
                if r1.val == r2.val: # both nodes have same value
                    stack.append([r1.left, r2.left]) # add the left children of both 
                                                        #nodes to the queue
                    stack.append([r1.right, r2.right]) # add the right children
                else: # nodes have same value
                    return False
            elif r1 or r2: # one of them is node and other is None
                return False
        return True # we have traversed all the nodes, 
    #                 # and all have same values

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(str(p))
        return str(p) == str(q)

        