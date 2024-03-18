from typing import List
import heapq

class Solution:
    # Sorting - O(nlogn) time; O(n) space
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        stack = []
        arrows = 0
        for point in points:
            if not stack or stack[-1][1] < point[0]:
                stack.append(point)
                arrows += 1
            else:
                stack[-1][1] = min(stack[-1][1], point[1])
        return arrows

    # Sorting - O(nlogn) time; O(1) space
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        previous_point = None
        arrows = 0
        for point in points:
            if not previous_point or previous_point[1] < point[0]:
                arrows += 1
                previous_point = point
            else:
                previous_point[1] = min(previous_point[1], point[1])
        return arrows

    # Sorting using heaps - O(nlogn) time; O(1) space
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heapq.heapify(points)
        arrows = 0
        previous_point = None
        while points:
            point = heapq.heappop(points)
            if not previous_point or previous_point[1] < point[0]:
                previous_point = point
                arrows += 1
            else:
                previous_point[1] = min(previous_point[1], point[1])
        return arrows

        