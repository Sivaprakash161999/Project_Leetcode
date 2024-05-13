from typing import List


class Solution:
    # - O(m * n) time; 
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def calculate_binary():
            score = 0
            for row in grid:
                num = 0
                for bit in row:
                    num = (num * 2) + bit
                score += num
            return score

        def toggle_row(row):
            for i in range(len(row)):
                row[i] ^= 1
        
        def toggle_col(col):
            zeros = 0
            for r in range(rows):
                if grid[r][col] == 0:
                    zeros += 1
            if zeros > (rows - zeros):
                for r in range(rows):
                    grid[r][col] ^= 1

        for row in grid:
            if row[0] == 0:
                toggle_row(row)
        for col in range(cols):
            toggle_col(col)
        return calculate_binary()
    


    # without modifying
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # set score to summation of first column
        score = (1 << (n - 1)) * m

        # loop over all other columns
        for j in range(1, n):
            count_same_bits = 0
            for i in range(m):
                # Count elements matching first in row
                if grid[i][j] == grid[i][0]:
                    count_same_bits += 1
            
            # Calculate score based on the number of same bits in a column
            count_same_bits = max(count_same_bits, m - count_same_bits)
            # Calculate the score contribution for the current column
            column_score = (1 << (n - j - 1)) * count_same_bits
            # Add contribution to score
            score += column_score
        return score


        