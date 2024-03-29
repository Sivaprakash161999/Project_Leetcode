from typing import List


class Solution:
    # sliding window + count; O(n) time; O(1) space
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxo = max(nums)
        prev_count = {}
        mx_count = 0
        subarrays = 0
        for right in range(len(nums)):
            if nums[right] == maxo:
                mx_count += 1
                prev_count[mx_count] = right
            if mx_count >= k:
                subarrays += prev_count.get(mx_count - k + 1, 0) + 1
        return subarrays

    # sliding window - O(n) time; O(1) space
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans = start = max_elements_in_window = 0
        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans

    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        indexes_of_max_elements = []
        ans = 0
        for index, element in enumerate(nums):
            if element == max_element:
                indexes_of_max_elements.append(index)
            freq = len(indexes_of_max_elements)
            if freq >= k:
                ans += indexes_of_max_elements[-k] + 1
        return ans

    # reverse logic
    # find subarrays with number of max element is < k
    # subtract this result from total subarrays
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)
        start = 0
        mx_count = 0
        subarray_lt_k = 0
        for end in range(n):
            if nums[end] == max_element:
                mx_count += 1
            while mx_count >= k:
                if nums[start] == max_element:
                    mx_count -= 1
                start += 1
            subarray_lt_k += (end - start + 1)
        total_subarrays = (n * (n + 1)) // 2
        return total_subarrays - subarray_lt_k

        