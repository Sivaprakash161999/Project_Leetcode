


class Solution:
    # odd number should have a '1' at its least significant bit
    # for a number to be large, all of its '1' should be towards
    # the left side
    # combining this 2 observations, we will keep one '1' at the
    # right most bit for 'oddity' and remaining all '1's will be
    # at the left most side; all the bits in the middle will be
    # filled with '0'
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')
        return  ('1' * (ones - 1)) + ('0' * (n - ones)) + '1'

    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ans = ['0'] * n
        j = 0
        for i in range(n):
            if s[i] == '1':
                ans[j] = '1'
                j += 1
        ans[j - 1] = '0'
        ans[-1] = '1'
        return ''.join(ans)
    
    # for both: Time - O(n)
    # for both: Space - O(n)