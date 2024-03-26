from typing import List


class Solution:
    # sets - O(n) time; O(n) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_st = set(nums)
        for num in range(1, len(nums) + 2):
            if num not in num_st:
                return num

    # sorting - O(nlogn) time; O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        pos = 1
        for num in nums:
            if num > 0:
                if num < pos:
                    continue
                if num != pos:
                    return pos
                pos += 1
        return pos

    # in-place - O(n) time; O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains_1 = False
        # Replace negative numbers, zeros,
        # and numbers larger than n with 1s.
        # After this nums contains only positive numbers.
        for i in range(n):
            # Check whether 1 is in the original array
            if nums[i] == 1:
                contains_1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if not contains_1:
            return 1
        # Mark whether integers 1 to n are in nums
        # Use index as a hash key and negative sign as a presence detector.
        for i in range(n):
            value = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            nums[value % n] = -abs(nums[value % n])

        # First positive in nums is smallest missing positive integer
        for i in range(1, n):
            if nums[i] > 0:
                return i
        # nums[0] stores whether n is in nums
        if nums[0] > 0:
            return n
        # If nums contained all elements 1 to n
        # the smallest missing positive number is n + 1  
        return n + 1

    # Cycle Sort - O(n) time; O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Use cycle sort to place positive elements smaller than n
        # at the correct index
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        # Iterate through nums
        # return smallest missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # If all elements are at the correct index
        # the smallest missing positive number is n + 1
        return n + 1      