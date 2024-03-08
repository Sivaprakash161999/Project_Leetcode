from collections import Counter
from typing import List


class Solution:
    # Counting - O(n) time; O(n) space
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = [0] * 101
        for num in nums:
            counter[num] += 1
        mx = max(counter)
        return sum([num for num in counter if num == mx])

    # Counting - O(n) time; O(n) space
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        mx = max(cnt.values())
        for num in cnt.values():
            if num == mx:
                ans += num
        return ans
        