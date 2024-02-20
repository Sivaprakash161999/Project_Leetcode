from operator import xor
from typing import List
from itertools import chain
from functools import reduce

class Solution:
    # Summation formula - O(n) time; O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        '''sum of first N natural number = (N) * (N + 1) // 2'''
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)

    # hash - O(n) time; O(n) space
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    # sorting - O(n) time; O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if i != nums[i]:
                return i
            i += 1
        return i
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    # Bit manipulation - O(n) time; O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        '''we take xor of all the num in nums and then,
           all the nums in range [1, nums];
           all the num in both these things will cancel out
           each other; only the missing number will be left

           i.e) a ^ a = 0'''
        mask = 0
        for num in nums:
            mask ^= num
        for num in range(1, len(nums) + 1):
            mask ^= num
        return mask
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in range(n):
            sum ^= (i^nums[i])
        return sum^n
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, chain(nums, range(len(nums) + 1)))

        

        