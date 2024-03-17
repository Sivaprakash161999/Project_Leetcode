from typing import List


class Solution:
    # O(n) time; O(n) space
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        stack = []
        inserted = False
        for start, end in intervals:
            if ((start <= newInterval[0] <= end) or start > newInterval[0]) and not inserted:
                stack.append(newInterval)
                inserted = True
            stack.append([start, end])
        stack2 = []
        for start, end in stack:
            if not stack2 or stack2[-1][1] < start:
                stack2.append([start, end])
            else:
                prev_start, prev_end = stack2.pop()
                new_start = min(prev_start, start)
                new_end = max(prev_end, end)
                stack2.append([new_start, new_end])
        return stack2

    # O(n) time; O(1) space
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after mergin newInterval
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

    # Binary search
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # If intervals is empty, just return a list with newInterval.
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        # Binary search to find the position to insert newInterval.
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Insert newInterval at the found position.
        intervals.insert(left, newInterval)

        # Merge overlapping intervals.
        res = []
        for interval in intervals:
            # If result is empty or there is no overlap, add the interval to the result
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # If there is an overlap, merge the intervals by updating the end of the
            # last interval in res
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res