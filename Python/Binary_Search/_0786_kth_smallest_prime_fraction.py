from typing import List
import heapq

class Solution:

    # brute force + heap - O(n**2) time; O(n) space
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                frac = arr[i] / arr[j]
                heapq.heappush(heap, (frac, [arr[i], arr[j]]))
        for _ in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)[1]


    # binary search - O(n.log(m^2)) time; O(1) space
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        left, right = 0, 1.0

        # Binary search for finding the kth smallest prime fraction
        while left < right:
            # Calculate the middle value
            mid = (left + right) / 2
            # Initialize variables to keep track of maximum fraction and indices
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1

            # Iterate thorugh the array to find fractions smaller than mid
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                # Count smaller fractions
                total_smaller_fractions += (n - j)

                # If we have exhausted the array, break
                if j == n:
                    break
                
                # Calculate the fraction
                fraction = arr[i] / arr[j]

                # Update max_fraction and indices if necessary
                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            # Check if we have found the kth smallest prime fraction
            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                right = mid # Adjust the range for binary search
            else:
                left = mid
        return [] # Return empth list if kth smallest prime fraction not found


    # priority queue - O((n + k).logn) time; O(n) space
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        # Create a priority queue to store pairs of fractions
        pq = [(arr[i]/arr[-1], i, n - 1) for i in range(n)]


        # Push the fractions formed by dividing each element by
        # the largest element into the priority queue
        heapq.heapify(pq)

        # Iteratively remove the top element (smallest fraction)
        # and replace it with the next smallest fraction
        for _ in range(k - 1):
            curr = heapq.heappop(pq)
            numerator_idx = curr[1]
            denominator_idx = curr[2] - 1
            if denominator_idx > numerator_idx:
                heapq.heappush(pq, 
                    (arr[numerator_idx] / arr[denominator_idx],
                    numerator_idx,
                    denominator_idx))
        # Retrieve the kth smallest fraction from
        # the top of the priority queue
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]


    # binary search
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = arr[0] / arr[-1], 1.0

        def smaller_m(value):
            nb_smallest_fraction = 0
            numer = arr[0]
            denom = arr[-1]
            slow = 0
            for fast in range(1, n):
                while slow < fast and arr[slow] / arr[fast] < value:
                    if arr[slow] / arr[fast] > numer / denom:
                        numer = arr[slow]
                        denom = arr[fast]
                    slow += 1
                nb_smallest_fraction += slow
            return [nb_smallest_fraction, numer, denom]

        while l < r:
            m = (l + r) / 2
            count, numer, denom = smaller_m(m)
            if count == k:
                return [numer, denom]
            elif count > k:
                r = m
            else:
                l = m
