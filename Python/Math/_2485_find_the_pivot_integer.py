import math


class Solution:
    # arithmetic series; O(logn) time; O(1) space
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        cur_sum = 0
        for x in range(n, 0, -1):
            cur_sum += x
            if cur_sum > total:
                return -1
            if cur_sum == total:
                return x
            total -= x

    # brute force: O(n^2) time; O(1) space
    def pivotInteger(self, n: int) -> int:
        # Iterate through possible pivot values
        for i in range(1, n + 1):
            # Calculate the sum of elements on the left side of the pivot
            sum_left = sum(range(1, i + 1))
            # Calculate the sum of elements on the right side of the pivot
            sum_right = sum(range(i, n + 1))

            # Check if the sums on both sides are equal
            if sum_left == sum_right:
                return i # Return the pivot value if found
        return -1 # Return -1 if no pivot is found

    # Two pointer: O(n) time; O(1) space
    def pivotInteger(self, n: int) -> int:
        left_value = 1
        right_value = n
        sum_left = left_value
        sum_right = right_value
        if n == 1:
            return n
        # Iterate until the pointers meet
        while left_value < right_value:
            # Adjust sums and pointers based on comparison
            if sum_left < sum_right:
                left_value += 1
                sum_left += left_value
            else:
                right_value -= 1
                sum_right += right_value

            # Check for pivot condition
            if sum_left == sum_right and left_value + 1 == right_value - 1:
                return left_value + 1
        return -1 # Return -1 if no pivot is found

    # Binary Search - O(logn) time; O(1) space
    def pivotInteger(self, n: int) -> int:
        # Initialize left and right pointer for binary search.
        left, right = 1, n

        # Calculate the total sum of the sequence.
        total_sum = n * (n + 1) // 2

        # Binary search for the pivot point
        while left < right:
            # Calculate the mid-point.
            mid = (left + right) // 2

            # Check if the difference between the squares of mid and the total sum is negative
            if mid * mid - total_sum < 0:
                left = mid + 1 # Adjust the left bound if the sum is smaller
            else:
                right = mid # Adjust the right bound if the sum is equal or greater

        # Check if the squares of the left pointerr minus the total sum is zero
        if left * left - total_sum == 0:
            return left
        else: 
            return -1

    # Precompute and Cache in a lookup Table
    maxValue = 1000
    # Array to store precomputed pivot values
    precompute = [0] * (maxValue + 1) # Initializing to 0

    # # O(m) time; O(m) space where m is the maxValue precomputed
    def pivotInteger(self, n: int) -> int:
        # Check if the precompute array is not initialized
        if self.precompute[1] == 0:
            for i in range(1, self.maxValue + 1):
                sum_val = i * (i + 1) // 2
                j = 1
                # Find the first square greater than or equal to sum
                while j * j < sum_val:
                    j += 1
                # Check if j * j is equal to sum (pivot found), Otherwise set to -1.
                self.precompute[i] = j if j * j == sum_val else -1

        return self.precompute[n]

    # Math - O(1) time; O(1) space
    def pivotInteger(self, n: int) -> int:
        sum = (n * (n + 1) // 2)
        pivot = int(math.sqrt(sum))
        # If pivot * pivot is equal to sum (pivot found) return pivot, else return -1
        return pivot if pivot * pivot == sum else -1



        