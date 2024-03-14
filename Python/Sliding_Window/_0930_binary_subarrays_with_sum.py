from typing import List

class Solution:
    # Prefix sum + all subarrays: O(n^2) time TLE; O(n) space
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nums[i]
        ans = 0
        for i in range(n + 1):
            if pref_sum[i] >= goal:
                for j in range(i):
                    cur_sum = pref_sum[i] - pref_sum[j]
                    if cur_sum == goal:
                        ans += 1
                    elif cur_sum < goal:
                        break
        return ans

    # Prefix sum - O(n) time; O(n) space
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        freq = {} # {prefix_sum: number of occurence}
        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1
            # Check if there is any prefix sum that can be subtracted from the 
            # current sum to get the desired goal
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]
            freq[current_sum] = freq.get(current_sum, 0) + 1
        return total_count

    # Sliding window 2 pass - O(n) time; O(1) space
    # Helper function to count the number of subarrays with sum at most the given goal
    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        start, current_sum, total_count = 0, 0, 0
        
        # Iterate through the array using sliding window approach
        for end in range(len(nums)):
            current_sum += nums[end]

            # Adjust the window by moving the start pointer to the right
            # until the sum becomes less than or equal to the goal
            while start <= end and current_sum > goal:
                current_sum -= nums[start]
                start += 1
            
            # Update the total count by adding the length of the current subarray
            total_count += end - start + 1
        return total_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)


    # Sliding Window 1 pass - O(n) time; O(n) space
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        prefix_zeros = 0
        current_sum = 0
        total_count = 0

        # Loop through the array using end pointer
        for end, num in enumerate(nums):
            # Add current element to the sum
            current_sum += num

            # Slide the window while condition is met
            while start < end and (nums[start] == 0 or current_sum > goal):
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1
                
                current_sum -= nums[start]
                start += 1
            
            # Count subarrays when window sum matches the goal
            if current_sum == goal:
                total_count += 1 + prefix_zeros

        return total_count