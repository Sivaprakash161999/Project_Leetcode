from collections import defaultdict
from typing import List


class Solution:
    # Helper function to count the number of subarrays with at most K distinct elements.
    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        # To store the occurence of each element
        freq_map = defaultdict(int)
        left = 0
        total_count = 0
        # Right pointer of the sliding window iterates through the array.
        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            # If the number of distinct elements in the window exceeds k,
            # we shrink the window from the left until we have at most k distinct elements.
            while len(freq_map) > distinctK:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # Update the total count by adding the length of the current subarray.
            total_count += right - left + 1
        return total_count

    # # sliding window + counting - O(n) time; O(n) space
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # atmost K - atmost (K - 1) == exactly K
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)


    # single pass sliding window - O(n) time; O(n) space
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Dictionary to store the count of distinct values encountered
        distinct_count = defaultdict(int)

        total_count = 0
        left = 0
        curr_count = 0
        for right in range(len(nums)):
            # Increment the count of the current element in the window
            distinct_count[nums[right]] += 1

            # If encountering a new distinct element, decrement K
            if distinct_count[nums[right]] == 1:
                k -= 1

            # If K becomes negative, we have more than K distinct elements
            # adjust the window from left
            if k < 0:
                # Move the left pointer until the count of distinct elements becomes
                # valid again
                distinct_count[nums[left]] -= 1
                if distinct_count[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0
            
            # If K becomes zero, calculate subarrays
            if k == 0:
                # While the count of left remains greater than 1, keep shrinking 
                # the window from left
                while distinct_count[nums[left]] > 1:
                    distinct_count[nums[left]] -= 1
                    left += 1
                    curr_count += 1
                # Add the count of subarrays with K distinct elements to the total count
                total_count += (curr_count + 1)
        return total_count