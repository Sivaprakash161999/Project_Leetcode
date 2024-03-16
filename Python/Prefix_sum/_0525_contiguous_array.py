from typing import List

class Solution:
    # prefix sum-hash table - O(n) time; O(n) space
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        pref_sum = {0: -1} 
        count = 0 # to track relative sum of 1 and 0; if 1 count++, if 0 count--
        for i, num in enumerate(nums):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in pref_sum:
                max_len= max(max_len, i - pref_sum[count])
            else:
                pref_sum[count] = i
        return max_len

    # more compact without conditionals
    def findMaxLength(self, nums: List[int]) -> int:
        ans, cnt, pref = 0, 0, {0: -1}
        for i, num in enumerate(nums):
            cnt += 2*num - 1
            ans = max(i - pref.setdefault(cnt, i), ans)
        return ans

        