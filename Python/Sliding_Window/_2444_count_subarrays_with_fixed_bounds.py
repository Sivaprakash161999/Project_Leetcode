from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        # bad_idx keeps track of last seen number index outside minK and maxK range
        # left_idx keeps track of last seen index of minK
        # right_idx keeps track of last seen index of maxK
        bad_idx = left_idx = right_idx = -1
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = i
            if num == minK:
                left_idx = i
            if num == maxK:
                right_idx = i
            # min(left_idx, right_idx) gives the left most index
            # that should be part of the subarray from our current postion
            # to be a valid subarray - (it contains both minK and maxK)
            # if the bad_idx is to the right of the above index,
            # then this subarray becomes invalid; we add 0
            # else, all the subarrays that starts after bad_idx
            # and upto the above idx are valid
            res += max(0, min(left_idx, right_idx) - bad_idx)
        return res