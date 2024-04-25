


class Solution:
    # DP - TLE - (2**n) time;
    # def longestIdealString(self, s: str, k: int) -> int:
    #     n = len(s)
    #     ans = [0]
    #     def dfs(curr_index, last_index, curr_length):
    #         if curr_index == n:
    #             ans[0] = max(ans[0], curr_length)
    #             return
    #         if last_index == -1:
    #             # select current index
    #             dfs(curr_index + 1, curr_index, curr_length + 1)
    #             # skip current index
    #             dfs(curr_index + 1, last_index, curr_length)
    #         else:
    #             # skip current index
    #             dfs(curr_index + 1, last_index, curr_length)
    #             # check if curr_index can be included
    #             if abs(ord(s[curr_index]) - ord(s[last_index])) <= k:
    #                 dfs(curr_index + 1, curr_index, curr_length + 1)
    #     dfs(0, -1, 0)
    #     return ans[0]

    # DP - memoization - O(n.l) time; O(n.l) space
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        # initialize all values to -1 to indicate non-visited states
        memo = [[-1] * 26 for _ in range(n)]

        def dfs(i: int, c: int) -> int:
            if memo[i][c] != -1:
                return memo[i][c]

            # State is not visited yet
            memo[i][c] = 0
            match = c == (ord(s[i]) - ord('a'))
            if match:
                memo[i][c] = 1

            # Non base case handling
            if i > 0:
                memo[i][c] = dfs(i - 1, c)
                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            memo[i][c] = max(memo[i][c], dfs(i - 1, p) + 1)
            return memo[i][c]

        # Find the maximum dp[n-1][c] and return the result
        res = 0
        for c in range(26):
            res = max(res, dfs(n-1, c))
        return res


    # DP - tabulation - (space optimized) - O(n*l) time; O(l) space
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26

        res = 0
        # updating dp with the ith character
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    best = max(best, dp[prev])
            
            # Append s[i] to the previous longest ideal subsequence
            dp[curr] = max(dp[curr], best + 1)
            res = max(res, dp[curr])
        return res
    

    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            l, r = max(0, cur - k), min(cur + k + 1, 26)
            dp[cur] = 1 + max([dp[j] for j in range(l, r)])
        return max(dp)

            
        