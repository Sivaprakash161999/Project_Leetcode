from typing import List
from functools import reduce
from operator import xor


class Solution:
    # bit manipulation - O(n) time; O(1) space
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        ops = 0
        while k or xor:
            if (xor & 1) != (k & 1):
                ops += 1
            xor >>= 1
            k >>= 1
        return ops

    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        # xor with k to find the mismatched bits
        diff = xor ^ k
        ops = 0
        # count the number of 1 in diff
        # n & (n - 1) will unset the right most set bit
        while diff:
            ops += 1
            diff &= (diff - 1)
        return ops

    def minOperations(self, nums: List[int], k: int) -> int:
        # initialize xor with k to skip the final comaprison
        xor = k
        for num in nums:
            xor ^= num
        # built in funciton bit_count to count set bits
        return xor.bit_count()

    def minOperations(self, nums: List[int], k: int) -> int:
        xor = k
        for num in nums:
            xor ^= num
        # bin to convert int into str and count number of 1
        return bin(xor).count('1')

    # use functools.reduce and operators.xor
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(xor, nums, k).bit_count()


        
        