import heapq

class Solution:
    # DP - if input size is 10^5 or more, never use dp
    # MLE - Memory Limit Exceeded
    # def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    #     n = len(heights)
    #     memo = {}
    #     def dfs(idx, bs, la):
    #         if idx == n - 1:
    #             return n - 1
            
    #         if (idx, bs, la) in memo:
    #             return memo[(idx, bs, la)]

    #         ans = idx
    #         if heights[idx + 1] <= heights[idx]:
    #             ans = max(ans, dfs(idx + 1, bs, la))
    #             memo[(idx, bs, la)] = ans
    #             return ans
    #         if la > 0:
    #             ans = max(ans, dfs(idx + 1, bs, la - 1))
    #         if heights[idx + 1] - heights[idx] <= bs:
    #             diff = heights[idx + 1] - heights[idx]
    #             ans = max(ans, dfs(idx + 1, bs - diff, la))
    #         memo[(idx, bs, la)] = ans
    #         return ans
    #     return dfs(0, bricks, ladders) 


    # Greedy + priority queue
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''It is optimal to use all the ladders and use them when the height difference is high.
            We will use up all the ladders, and store the height differences in 
            a priority queue or min heap of length 'ladders'. Whenever the 
            length of the pq, goes over 'ladders', we will pop the minimum difference
            from the pq and reduce it from the bricks, until we run out of bricks'''
        n = len(heights)
        hp = []
        heapq.heapify(hp)
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(hp, diff)
            if len(hp) > ladders:
                bricks -= heapq.heappop(hp)
            if bricks < 0:
                return i
        return n - 1
                

        