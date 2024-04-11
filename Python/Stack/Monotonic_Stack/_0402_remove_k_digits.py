

class Solution:
    # monotonic increasing stack - O(n) time; O(n) space
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        The digits in the smallest result 
        will be in increasing order.
        Maintain a monotonic increasing stack,
        and pop upto k elemnents.
        If the numbers are already monotonically increasing
        pop the last k numbers
        '''
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            if not stack and ch == "0": # will skip the leading zeroes
                continue
            stack.append(ch)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        return res if res else "0"
        
        