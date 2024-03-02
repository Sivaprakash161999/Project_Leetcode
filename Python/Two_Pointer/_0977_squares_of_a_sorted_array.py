from typing import List
from collections import Counter


class Solution:
    # sorting - time: O(nlogn), space: O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [num**2 for num in nums]
        ans.sort()
        return ans

    # counting sort - time: O(n); space: O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        count = [0] * (10**4 + 1)
        for num in nums:
            if num < 0:
                num = -num
            count[num] += 1
        ans = []
        for i in range(len(count)):
            if count[i]:
                for _ in range(count[i]):
                    ans.append(i*i)
        return ans

    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter([abs(x) for x in nums])
        for num in sorted(count.keys()):
            ans.extend([num*num] * count[num])
        return ans

    # two-pointer - time: O(n); space: O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        for i in range(n):
            if abs(nums[l]) >= abs(nums[r]):
                ans[n - i - 1] = nums[l] * nums[l]
                l += 1
            else:
                ans[n - i - 1] = nums[r] * nums[r]
                r -= 1
        return ans


        