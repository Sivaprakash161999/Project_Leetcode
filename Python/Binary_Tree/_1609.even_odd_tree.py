from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # BFS
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.val % 2 == 0:
            return False

        q = deque()
        q.append(root)
        lev_idx = 1
        while q:
            new_q = []
            for _ in range(len(q)):
                curr = q.popleft()
                lc = curr.left 
                rc = curr.right
                if lev_idx % 2 == 0:
                    if (lc and lc.val % 2 == 0) or (rc and rc.val % 2 == 0):
                        return False
                    if lc and new_q and new_q[-1].val >= lc.val:
                        return False
                    if lc:
                        new_q.append(lc)
                    if rc and new_q and new_q[-1].val >= rc.val:
                        return False
                    if rc:
                        new_q.append(rc)
                else:
                    if (lc and lc.val % 2 == 1) or (rc and rc.val % 2 == 1):
                        return False
                    if lc and new_q and new_q[-1].val <= lc.val:
                        return False
                    if lc:
                        new_q.append(lc)
                    if rc and new_q and new_q[-1].val <= rc.val:
                        return False
                    if rc:
                        new_q.append(rc)
            q = deque(new_q)
            lev_idx += 1
        return True

    # DFS
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev = []
        def dfs(current, level):
            # Base case, an empty tree is Even-Odd
            if not current:
                return True

            # Compare the parity of current and level
            if current.val % 2 == level % 2:
                return False
            
            # Add a new level to prev if we've reached a new level
            while len(prev) <= level:
                prev.append(0)
            # If there are previous nodes on this level, check increasing/decreasing
            # If on an even level, check that current's value is greater than the previous on this level
            # If on an odd level, check that current's value is less than the previous on this level
            if prev[level] != 0 and ((level % 2 == 0 and current.val <= prev[level])
                                        or (level % 2 == 1 and current.val >= prev[level])):
                return False
            # Add current value to prev at index level
            prev[level] = current.val

            # Recursively call DFS on the left and right children
            return dfs(current.left, level + 1) and dfs(current.right, level + 1)
        return dfs(root, 0)

    # BFS - more clean
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Create a queue for nodes that need to be visited and add the root
        queue = deque()
        current = root
        queue.append(current)

        # Keeps track of whether we are on an even level
        even = True

        # While there are more nodes in the queue
        # Determine the size of the level and handle the nodes
        while queue:
            size = len(queue)

            # Prev holds the value of the previous node in this level
            prev = float('inf')
            if even:
                prev = float('-inf')

            # While there are more nodes in this level
            # Remove a node, check whether it satisfies the conditions
            # Add its children to the queue
            while size > 0:
                current = queue.popleft()

                # If on an even level, check that the node's value is odd and greater than prev
                # If on an odd level, check that the node's value is even and less than prev
                if (even and (current.val % 2 == 0 or current.val <= prev)) or \
                    (not even and (current.val % 2 == 1 or current.val >= prev)):
                    return False
            
                prev = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                # Decrement size, we have handled a node on this level
                size -= 1

            # Flip the value of even, the next level will be opposite
            even = not even
        # If every node meets the conditions, the tree is Even-Odd
        return True





            







            
