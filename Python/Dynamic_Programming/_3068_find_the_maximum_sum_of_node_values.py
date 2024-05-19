from typing import List


class Solution:
    # top down dp - O(n) time; O(n) space
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        def dfs(idx, is_even):
            # If the operation is performed on an odd number of 
            # elements return INT_MIN
            if idx == n:
                return 0 if is_even == 1 else float('-inf')

            if memo[idx][is_even] != -1:
                return memo[idx][is_even]

            # No operation performed on the element
            no_xor_done = nums[idx] + dfs(idx + 1, is_even)

            # XOR operation performed on the element
            xor_done = (nums[idx] ^ k) + dfs(idx + 1, is_even ^ 1)

            memo[idx][is_even] = max(xor_done, no_xor_done)
            return memo[idx][is_even] 

        memo = [[-1] * 2 for _ in range(len(nums))]
        return dfs(0, 1)


    # bottom up dp - O(n) time; O(n) space
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        dp[n][0] = float('-inf')

        for idx in range(n - 1, -1, -1):
            for is_even in range(2):
                # Case 1: we perform an operation on this element.
                perform_operation = (nums[idx] ^ k) + dp[idx + 1][is_even ^ 1]
                dont_perform_operation = nums[idx] + dp[idx + 1][is_even]
                dp[idx][is_even] = max(perform_operation, dont_perform_operation)
        return dp[0][1]

    # Greedy + sorting - O(nlogn) time; O(n) space
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        net_change = [(nums[i] ^ k) - nums[i] for i in range(n)]
        node_sum = sum(nums)

        net_change.sort(reverse=True)
        for i in range(0, n, 2):
            # If net_change contains odd number of elements break the loop
            if i + 1 == n:
                break
            pair_sum = net_change[i] + net_change[i + 1]
            # Include in node_sum if pair_sum is positive
            if pair_sum > 0:
                node_sum += pair_sum
        return node_sum

    # Greedy
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum_val = 0
        count = 0
        positive_minimum = 1 << 30
        negative_maximum = -1 * (1 << 30)

        for node_val in nums:
            operated_node_value = node_val ^ k
            sum_val += node_val
            net_change = operated_node_value - node_val
            if net_change > 0:
                positive_minimum = min(positive_minimum, net_change)
                sum_val += net_change
                count += 1
            else:
                negative_maximum = max(negative_maximum, net_change)

        # If the number of positive net_change values is even, return sum
        if count % 2 == 0:
            return sum_val
        
        # Otehrwise return the maximum of both discussed cases.
        return max(sum_val - positive_minimum, sum_val + negative_maximum)

        