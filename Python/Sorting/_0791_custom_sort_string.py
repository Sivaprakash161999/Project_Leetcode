from collections import defaultdict

class Solution:
    # counting sort - O(n + m) time; O(26) space
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans = []
        for c in order:
            idx = ord(c) - ord('a')
            if count[idx]:
                ans.extend([c] * count[idx])
                count[idx] = 0
        for idx in range(26):
            if count[idx]:
                c = chr(ord('a') + idx)
                ans.extend([c] * count[idx])
                count[idx] = 0
        return ''.join(ans)

    # hash map and custom comparator - O(nlogn) time; O(26) space
    def customSortString(self, order: str, s: str) -> str:
        h = defaultdict(int)
        for i, c in enumerate(order):
            h[c] = i
        return ''.join(sorted(list(s), key=lambda x:h[x]))
        