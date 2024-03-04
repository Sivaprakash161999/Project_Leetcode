from typing import List


class Solution:
    # Greedy + Sorting + Two Pointer: time - O(n), space - O(1)
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        cur, ans = 0, 0
        l, r = 0, n - 1
        tokens.sort()
        while l <= r and (power > tokens[l] or cur) :
            while l <= r and power >= tokens[l]:
                power -= tokens[l]
                cur += 1
                ans = max(ans, cur)
                l += 1
            if cur > 0 and r >= l:
                power += tokens[r]
                r -= 1
                cur -= 1
        return ans

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        l, r = 0, n - 1
        ans = 0
        tokens.sort()
        while l <= r:
            # When we have enough power, play lowest token face-up
            if power >= tokens[l]:
                ans += 1
                power -= tokens[l]
                l += 1
            # We don't have enough power to play a token face-up
            # If there is at least one token remaining,
            # and we have enough score, play highest token face-down
            elif l < r and ans > 0:
                ans -= 1
                power += tokens[r]
                r -= 1
            # We don't have enough score, power, or tokens 
            # to play face-up or down and increase our score
            else:
                return ans
        return ans



        