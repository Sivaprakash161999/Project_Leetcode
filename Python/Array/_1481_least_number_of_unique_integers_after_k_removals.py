from collections import Counter
import heapq
from typing import List


class Solution:
    # Sorting
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''Count the frequency of each number.
           Sort the frequencies;
           Start removing elements with lowest frequencies upto K elements.
           Return the number of remaining elements'''
        c = Counter(arr)
        ans = len(c)
        for f in sorted(c.values()):
            if f <= k:
                k -= f
                ans -= 1
            else:
                return ans
        return ans

    # another approach - using min heap
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''using a heap, instead of sorting
            to pick elements with least frequency.'''
        c = Counter(arr)
        ans = len(c)
        freq = list(c.values())
        heapq.heapify(freq)
        while freq:
            ele = heapq.heappop(freq)
            if ele <= k:
                k -= ele
                ans -= 1
            else:
                break
        return ans