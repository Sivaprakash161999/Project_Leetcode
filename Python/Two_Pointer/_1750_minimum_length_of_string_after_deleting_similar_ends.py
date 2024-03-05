


class Solution:
    # Two pointer
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l <= r:
            if s[l] != s[r]:
                return (r - l + 1)
            if l == r:
                return 1
            tmp = s[l]
            while l <= r and s[l] == tmp:
                l += 1
            while r >= l and s[r] == tmp:
                r -= 1
        
        return 0

    # two-pointer - iteration - Time: O(n), space: O(1)
    def minimumLength(self, s: str) -> int:
        begin = 0
        end = len(s) - 1

         # Delete similar ends until the ends differ or they meet in the middle
        while begin < end and s[begin] == s[end]:
            c = s[begin]

             # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

        # Return the number of remaining characters
        return end - begin + 1

    # tail recursion - time: O(n), space: O(n) - recursion stack space
    def minimumLength(self, s: str) -> int:
        return self.delete_similar_ends(s, 0, len(s) - 1)

    def delete_similar_ends(self, s: str, begin: int, end: int) -> int:
        # The ends differ or meet in the middle
        if begin >= end or s[begin] != s[end]:
            return end - begin + 1
        else:
            c = s[begin]

            while begin <= end and s[begin] == c:
                begin += 1

            while end > begin and s[end] == c:
                end -= 1

            return self.delete_similar_ends(s, begin, end)

        
            
