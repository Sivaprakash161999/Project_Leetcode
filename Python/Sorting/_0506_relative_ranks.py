from typing import List
import heapq
from collections import defaultdict


class Solution:
    # sorting - O(nlogn) time; O(n) space
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [0] * n
        place = 1
        for i, score in sorted(list(enumerate(score)), reverse=True, key= lambda x: x[1]):
            if place == 1:
                res[i] = "Gold Medal"
            elif place == 2:
                res[i] = "Silver Medal"
            elif place == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(place)
            place += 1
        return res


    # sorting + hashmap - O(nlogn) time; O(n) space
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score_to_index = defaultdict(int)
        for i in range(n):
            score_to_index[score[i]] = i
        ranks = [" "] * n
        score.sort(reverse=True)
        for i in range(n):
            if i == 0:
                ranks[score_to_index[score[i]]] = "Gold Medal"
            elif i == 1:
                ranks[score_to_index[score[i]]] = "Silver Medal"
            elif i == 2:
                ranks[score_to_index[score[i]]] = "Bronze Medal"
            else:
                ranks[score_to_index[score[i]]] = str(i + 1)
        return ranks


    # max heap - O(nlogn) time; O(n) space
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = []
        for i, sc in enumerate(score):
            heapq.heappush(heap, (-sc, i))

        rank = [" "] * n
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place += 1
        return rank


    # bucket sort - O(n + m) time; O(m) space
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        m = max(score)
        score_to_index = [-1] * (m + 1)
        for i in range(n):
            score_to_index[score[i]] = i
        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        place = 1
        rank = [" "] * n
        for score in range(m, -1, -1):
            if score_to_index[score] != -1:
                if place < 4:
                    rank[score_to_index[score]] = MEDALS[place - 1]
                else:
                    rank[score_to_index[score]] = str(place)
                place += 1
        return rank



        