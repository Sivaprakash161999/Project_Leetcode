

class Solution:
    # stack - O(n) time; O(n) space
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            # Push the character to stack,
            # if the stack is empty
            # if the character is same as last character and the case is also same
            # if the character is different as last character
            if not stack or stack[-1] == c or stack[-1].lower() != c.lower():
                stack.append(c)
            # If none of the above conditions met,
            # then the character is same as previous character
            # and the case is different
            # which makes the string bad
            # so, pop the last pushed character and continue to next character in s
            else:
                stack.pop()
        return ''.join(stack)
        