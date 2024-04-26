from typing import List


class Solution:
    # dp - tabulation O(n**3) time; O(n) space
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[n - 1][:]
        for row in range(n - 2, -1, -1):
            new_dp = [float('inf')] * n
            for col in range(n):
                for ic in range(n):
                    if col == ic:
                        continue
                    new_dp[col] = min(new_dp[col], dp[ic])
                new_dp[col] += grid[row][col]
            dp = new_dp
            # print(dp)
        return min(dp)


    # dp - O(n**2) time; O(n) space
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        def find_two_smallest_index(row):
            if row[0] <= row[1]:
                idx1, idx2 = 0, 1
            else:
                idx1, idx2 = 1, 0
            for i in range(2, n):
                if row[i] < row[idx1]:
                    idx1, idx2 = i, idx1
                elif row[i] < row[idx2]:
                    idx2 = i
            return idx1, idx2

        dp = grid[n - 1][:]
        for row in range(n - 2, -1, -1):
            new_dp = grid[row][:]
            idx1, idx2 = find_two_smallest_index(dp)
            val1, val2 = dp[idx1], dp[idx2]
            for col in range(n):
                if col == idx1:
                    new_dp[col] += val2
                else:
                    new_dp[col] += val1
            dp = new_dp
        return min(dp)
        