from typing import List


class Solution:
    # sorting + greedy - O(nlogn) time; O(1) space
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        selected = 0
        max_happiness = 0
        for i in range(k):
            max_happiness += max(0, happiness[i] - selected)
            selected += 1
        return max_happiness
    

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_happiness = 0
        for i in range(k):
            max_happiness += max(0, happiness[i] - i)
        return max_happiness
    

    # sorting + math
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        children = sorted(happiness, reverse=True)

        # fast calc if no children hits zero happiness
        if children[k - 1] >= (k - 1):
            return sum(children[:k]) - ((0 + (k - 1)) * k // 2)
        
        # else slow calc
        res = 0
        for i, h in enumerate(children):
            if h - i <= 0:
                return res
            res += (h - i)
        return res


        