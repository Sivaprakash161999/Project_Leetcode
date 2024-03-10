from typing import List


class Solution:
    # sets - O(n+m) time; O(n+m) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

    # hashsets - O(n+m) time; O(n) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = set(nums2)
        nums1 = set(nums1)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ans = set([num for num in nums1 if num in nums2])
        return list(ans)

    # sorting and two-pointer - O(nlogn+mlogm) time; O(1) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if (nums1[0] > nums2[-1]) or (nums2[0] > nums1[-1]):
            return []
        i, j = 0, 0
        ans = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(ans)

    # Counting Sort - O(n+m) time; O(n) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = [0] * 10001
        for num in nums1:
            count[num] += 1
        ans = set()
        for num in nums2:
            if count[num]:
                ans.add(num)
        return list(ans)

    # binary search - O(nlogm) time; O(1) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(target, nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        nums1.sort()
        if nums1[-1] < min(nums2):
            return []
        ans = set()
        for num in nums2:
            if binary_search(num, nums1):
                ans.add(num)
        return list(ans)

    # hashmap - O(m+n) time; O(n) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []
        for x in nums1:
            seen[x] = 1
        for x in nums2:
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0
        return result
        