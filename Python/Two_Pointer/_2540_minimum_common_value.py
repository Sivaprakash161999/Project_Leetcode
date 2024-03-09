from typing import List

class Solution:
    # Two-pointer: O(n+m) time; O(1) space
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1

    # hash set: O(n+m) time; O(n) space
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                return num
        return -1

    # sets
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)
        if common:
            return min(common)
        else:
            return -1

    # Binary Search - time: O(nlogm); space: O(1)
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(target, nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False

        # Binary search should be done on the larger array
        # If nums1 is longer, call getCommon with the arrays swapped
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)
        
        # Search for each element of nums1 in nums2
        # Return the first common element found
        for num in nums1:
            if binary_search(num, nums2):
                return num
        # Return -1 if there are no common elements
        return -1

        
        