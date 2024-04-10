from typing import List
from collections import deque


class Solution:
    # Two pointer + sorting (multiple pass) - O(nlogn) time; O(n) space
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] * n
        skip = False
        index_in_deck = 0
        index_in_result = 0

        deck.sort()
        while index_in_deck < n:
            # There is an available gap in result
            if result[index_in_result] == 0:
                # Add a card to result
                if not skip:
                    result[index_in_result] = deck[index_in_deck]
                    index_in_deck += 1
                
                # Toggle the skip to alternate between adding and skipping cards
                skip = not skip
            # Progress to the next index of result array
            index_in_result = (index_in_result + 1) % n
        return result

    # simulation with queue + sorting - O(nlogn) time; O(n) space
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque([i for i in range(n)]) # Queue of indices
        deck.sort()
        res = [0] * n # Put cards at correct index in result
        for card in deck:
            # Reveal Card
            res[queue.popleft()] = card

            # Move next card's index to bottom
            if queue:
                queue.append(queue.popleft())
        return res

    # reverse sorting + induction - O(nlogn) time; O(n) space
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        res = deque()
        for num in deck:
            if len(res) > 1:
                res.appendleft(res.pop())
            res.appendleft(num)
        return res
        