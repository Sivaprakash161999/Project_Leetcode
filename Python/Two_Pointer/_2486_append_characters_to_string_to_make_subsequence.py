

class Solution:
    # two-pointer - O(n) time; O(1) space
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        i, j = 0, 0

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        # return 0 if j == m else (m - j)
        return m - j
        