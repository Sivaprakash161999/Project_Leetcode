from typing import List


class Solution:
    # Backtracking - O(m*n*4^l) time - O(l) space where l is the length of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        visited = set() # to keep track of visited cells

        def dfs(row, col, i):
            '''
            row - current row in the board
            col - current col in  the board
            i - current index in the board
            '''
            # word found
            if i == n:
                return True
            # cells out of bounds
            if (not (0 <= row < ROWS) or 
                not (0 <= col < COLS) or
                (row, col) in visited or
                board[row][col] != word[i]):
                return False
            
            # Backtracking
            # add the current cell in visited
            visited.add((row, col))
            found = (dfs(row + 1, col, i + 1) or
                        dfs(row, col + 1, i + 1) or
                        dfs(row - 1, col, i + 1) or
                        dfs(row, col - 1, i + 1))
            # remove the current cell from visited
            visited.remove((row, col))
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        