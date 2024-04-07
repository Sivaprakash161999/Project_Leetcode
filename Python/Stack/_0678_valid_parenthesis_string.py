

class Solution:
    # Recursion - TLE - O(3**n) time; O(n) space
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        def dfs(i, count):
            '''
            i - current index of the string s
            count - relative count of opening and closing brackets
            '''
            if i == n:
                if count == 0:
                    return True
                return False
            if count < 0:
                return False
            if s[i] == '(':
                return dfs(i + 1, count + 1)
            elif s[i] == ')':
                return dfs(i + 1, count - 1)
            return any([dfs(i + 1, count + 1), dfs(i + 1, count - 1), dfs(i + 1, count)])
        return dfs(0, 0)

    # Dynamic Programming - Memoization - O(n*n) time; O(n*n) space for dp table
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = {}
        def dfs(i, count):
            if i == n:
                return count == 0
            if count < 0:
                return False
            if (i, count) in dp:
                return dp[(i, count)]
            if s[i] == '(':
                dp[(i, count)] = dfs(i + 1, count + 1)
            elif s[i] == ')':
                dp[(i, count)] = dfs(i + 1, count - 1)
            else:
                dp[(i, count)] = (dfs(i + 1, count + 1) or dfs(i + 1, count - 1)
                                    or dfs(i + 1, count))
            return dp[(i, count)]
        return dfs(0, 0)

    # Dynamic Programming - Tabulation - O(n * n) time; O(n * n) space
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # dp[i][j] represents if the substring starting from index i is valid 
        # with j opening brackets
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        # base case: an empty string with 0 opening brackets is valid
        dp[n][0] = True
        
        for index in range(n - 1, -1, -1):
            for open_brackets in range(n):
                is_valid = False
                # '*' can represent '(' or ')' or '' (empty)
                if s[index] == '*':
                    if open_brackets < n:
                        is_valid |= dp[index + 1][open_brackets + 1] # try '*' as '('
                    # opening brackets to use '*' as ')'
                    if open_brackets > 0:
                        is_valid |= dp[index + 1][open_brackets - 1] # try '*' as ')'
                    is_valid |= dp[index + 1][open_brackets] # ignore '*' 
                else:
                    # If the character is not '*', it can be '(' or ')'
                    if s[index] == '(':
                        is_valid |= dp[index + 1][open_brackets + 1] # try '('
                    elif open_brackets > 0:
                        is_valid |= dp[index + 1][open_brackets - 1] # try ')'
                dp[index][open_brackets] = is_valid
        return dp[0][0] # check if the entire string is valid with no excess opening brackets


    # Two Stacks - O(n) time; O(n) space
    def checkValidString(self, s: str) -> bool:
        # Stack to store indices of open brackets and asterisks
        open_brackets = []
        asterisks = []

        for i, ch in enumerate(s):
            # If current character is an open bracket, push its index onto the stack
            if ch == '(':
                open_brackets.append(i)
            # If current character is an ansterisk, push its index onto the stack
            elif ch == '*':
                asterisks.append(i)
            # current character is a closing bracket ')'
            else:
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    # unmatched ')' and no '*' to balance it.
                    return False
            
        # Check if there are remaining open brackets and asterisks that can balance them
        while open_brackets and asterisks:
            # If an open bracket appears after and asterisk, it cannot be balanced, 
            # return False
            if open_brackets.pop() > asterisks.pop():
                return False # '*' before '(' which cannot be balanced.
        # If all open brackets are matched and there are no unmatched open brackets left,
        # return true
        return not open_brackets


    # Two-pointer - O(n) time; O(1) space
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1
        # Traverse the string from both ends simulataneously
        for i in range(length + 1):
            # Count open parentheses or asterisks
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            # Count close parentheses or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1
            
            # If at any point open count or close count goes negative, 
            # the string is invalid
            if open_count < 0 or close_count < 0:
                return False

        # If open count and close count both are non-negative, 
        # the string is valid
        return True

