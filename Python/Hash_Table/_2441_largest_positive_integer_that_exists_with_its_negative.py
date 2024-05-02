from typing import List

class Solution:
    # set - O(n) time; O(n) space
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if -num in nums and num > res:
                res = num
        return res if res else -1

    # two-pointer - O(nlogn) time; O(1) space
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if -nums[lo] == nums[hi]:
                return nums[hi]
            elif -nums[lo] > nums[hi]:
                lo += 1
            else:
                hi -= 1
        return -1

    def findMaxK(self, nums: List[int]) -> int:
        seen = [0] * 1001
        res = -1
        for num in nums:
            abs_num = abs(num)
            if seen[abs_num] == -num:
                res = max(res, abs_num)
            seen[abs_num] = num
        return res
        