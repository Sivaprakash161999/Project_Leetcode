from collections import deque


class Solution:
    # Stack + hashsets - O(n) time; O(n) space
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = set()
        stack = [] # (idx of the open brackets)
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if not stack:
                    invalid.add(i)
                else:
                    stack.pop()
        for i in stack:
            invalid.add(i)
        return ''.join([s[i] for i in range(len(s)) if i not in invalid])


    # two traversals and counter - O(n) time; O(n) space
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        invalid = [1] * n
        count = 0
        for i, c in enumerate(s):
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    invalid[i] = 0
                else:
                    count -= 1
        count = 0
        for i, c in reversed(list(enumerate(s))):
            if c == ')':
                count += 1
            elif c == '(':
                if count == 0:
                    invalid[i] = 0
                else:
                    count -= 1
        return ''.join(s[i] for i in range(n) if invalid[i])


    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = deque()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)

        