

class Solution:
    # summation - O(n) time; O(1) space
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        want = tickets[k]
        time = 0
        for i in range(len(tickets)):
            # All the person before kth person
            # would have bought atmost tickets[k] tickets
            if i < k:
                time += min(tickets[i], want)
            # All the person after kth person
            # would have bought atmost tickets[k] - 1 tickets
            elif i > k:
                time += min(tickets[i], want - 1)
            else:
                time += want
        return time
        