from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # dfs + post order - O(n) time; O(n) space
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = [0]
        def dfs(node):
            if not node:
                return 0

            # calculate the coins each subtree has available to exchange
            left_coins = dfs(node.left)
            right_coins = dfs(node.right)
            
            # Add the total number of exchanges to moves
            moves[0] += abs(left_coins) + abs(right_coins)

            # The number of coins current has available to exchange
            return (node.val - 1) + left_coins + right_coins
        dfs(root)
        return moves[0]


        