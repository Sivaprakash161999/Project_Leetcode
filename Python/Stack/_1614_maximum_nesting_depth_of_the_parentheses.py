


class Solution:
    # stack - O(n) time; O(n) space
    def maxDepth(self, s: str) -> int: 
        depth = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
                depth = max(depth, len(stack))
            elif char == ')':
                stack.pop()
        return depth

    # counter - O(n) time; O(1) space
    def maxDepth(self, s: str) -> int:
        depth = 0
        curr = 0
        for char in s:
            if char == '(':
                curr += 1
                depth = max(depth, curr)
            elif char == ')':
                curr -= 1
        return depth

    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0
        for i in s:
            count += 1*(i=="(") - 1*(i==")")
            ans = max(ans, count)
        return ans