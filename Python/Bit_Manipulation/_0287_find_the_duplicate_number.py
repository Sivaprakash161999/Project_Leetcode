from typing import List

class Solution:
    # # using bit masking - mask can be a very large number - can be only implemented in python
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 1 << (n + 1)
        for num in nums:
            if (1 << num) & mask:
                return num
            mask = mask | (1 << num)

    # using set
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    # using count array
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = [0] * (len(nums) + 1)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > 1:
                return num

    # marking in array
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]

    # fast and slow pointer - Floyd's hare and tortoise
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]  # initialize slow and fast pointers to the first value
        
        while True:
            slow = nums[slow] # slow moves 1 step
            fast = nums[nums[fast]] # fast moves 2 steps
            if slow == fast: # slow and fast will meet at some place in the cycle
                break  

        slow = nums[0] # again initiate slow; keep fast at the last intersection
        while slow != fast:
            slow = nums[slow]  # now both slow and fast moves at same speed
            fast = nums[fast] # they will meet at the starting point of the cycle; which 
                                # is the duplicate
        return slow

    # binary search
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1 # initiate low to 1 and high to n

        while low < high:
            mid = (low + high) // 2 # find mid
            count = 0
            for num in nums: # scan the array, and count numbers less than mid
                if num <= mid:
                    count += 1
            if count > mid: # if count > mid, duplicate is in left bound
                high = mid
            else:            # else, duplicate in right bound
                low = mid + 1
        return low

    # sorting
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    # bit masking - optimized
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        bit_max = 31
        while (n - 1) >> bit_max == 0:
            bit_max -= 1              # setting the max required bit mask, based on the 
                                                # max element of the array
        for bit in range(bit_max + 1):
            x, y = 0, 0
            for i in range(n):
                if nums[i] & (1 << bit) != 0: # increase x, if the i the element has its
                                                # bit th bit set
                    x += 1
                if i >= 1 and (i & (1 << bit)) != 0: # increase y, if the number i has its
                                                    # bit th bit set
                    y += 1
            if x > y:    # if x > y, then this bit is part of the duplicate
                ans |= (1 << bit)
        return ans


        


