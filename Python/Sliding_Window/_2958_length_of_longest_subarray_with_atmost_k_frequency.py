from collections import Counter
from typing import List


class Solution:
    # counting and sliding window - O(n) time; O(n) space
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, start = 0, -1
        frequency = Counter()
        for end in range(len(nums)):
            frequency[nums[end]] += 1
            while frequency[nums[end]] > k:
                start += 1
                frequency[nums[start]] -= 1
            ans = max(ans, end - start)
        return ans

    # counting and sliding window - without inner loops
    # O(n) time; O(n) space
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequency = Counter()
        start = 0
        chars_with_freq_over_k = 0
        for end in range(n):
            frequency[nums[end]] += 1
            if frequency[nums[end]] == k + 1:
                chars_with_freq_over_k += 1
            if chars_with_freq_over_k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == k:
                    chars_with_freq_over_k -= 1
                start += 1
        return n - start
        