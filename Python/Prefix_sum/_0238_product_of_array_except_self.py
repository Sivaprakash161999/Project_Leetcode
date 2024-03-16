from typing import List


class Solution:
    # prefix and suffix arrays - O(n) time; O(n) space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        suff = [0] * n
        suff[-1] = nums[-1]
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i]
        # print(pref, suff)
        ans = [0] * n
        for i in range(n):
            ans[i] = (pref[i - 1] if i > 0 else 1) * (suff[i + 1] if i < (n - 1) else 1)
        return ans

    # prefix and suffix without extra space - O(n) time; O(1) space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix_product = 1
        for i in range(1, n):
            prefix_product *= nums[i - 1]
            ans[i] *= prefix_product
        suffix_product = 1
        for i in range(n - 2, -1, -1):
            suffix_product *= nums[i + 1]
            ans[i] *= suffix_product
        return ans

    
        