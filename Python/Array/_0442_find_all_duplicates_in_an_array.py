from typing import List


class Solution:
    # Sets - O(n) time; O(n) space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = set()
        res = []
        for num in nums:
            if num in unique:
                res.append(num)
            else:
                unique.add(num)
        return res

    # Sorting - O(nlogn) time; O(1) space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])
        return res

    # Flipping values - O(n) time; O(1) space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res
        