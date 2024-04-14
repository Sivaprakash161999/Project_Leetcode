from typing import List


class Solution:
    # two-pointers - O(n) time; O(n) space
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # left keeps track of the highest index encountered until current index from left
        # right keeps track of the highest index encountered until current index from right
        left, right = 0, n - 1
        # stores values for the heights heights in both direction 
        # for the current index
        left_high = [0] * n
        right_high = [0] * n
        water_units = 0
        for i in range(n):
            if height[i] > height[left]:
                left = i
            if height[n - 1 - i] > height[right]:
                right = n - 1 - i
            left_high[i] = height[left]
            right_high[n - 1 - i] = height[right]
        for i in range(n):
            water_units += max(0, min(left_high[i], right_high[i]) - height[i])
        return water_units 


    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left = [0] * n
        right = [0] * n
        # Fill left array
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        # Fill right array
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])       
        # Calculate trapped water
        trappedWater = 0
        for i in range(n):
            trappedWater += min(left[i], right[i]) - height[i] 
        return trappedWater
            
        