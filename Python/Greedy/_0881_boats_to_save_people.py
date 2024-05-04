from typing import List


class Solution:
    # sorting + greedy + two-pointer - O(nlogn) time; O(1) space
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if people[j] >= limit or (people[j] + people[i]) > limit:
                j -= 1
            else:
                j -= 1
                i += 1
            boats += 1
        return boats

        