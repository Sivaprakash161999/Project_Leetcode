from collections import defaultdict
import heapq


class Solution:
    # graph - bfs - wrong
    # def findRotateSteps(self, ring: str, key: str) -> int:
    #     n = len(ring)
    #     def bfs():
    #         curr_steps = 0
    #         while queue:
    #             for _ in range(len(queue)):
    #                 idx = queue.popleft()
    #                 left, right = (idx - 1) % n, (idx + 1) % n
    #                 if ring[idx] == target:
    #                     return curr_steps, [idx]
    #                 if left not in visited:
    #                     visited.add(left)
    #                     queue.append(left)
    #                 if right not in visited:
    #                     visited.add(right)
    #                     queue.append(right)
    #             curr_steps += 1

    #     steps = 0 # to track number of steps
    #     source_idx = [0]
    #     for target in key:
    #         queue = deque(source_idx)
    #         visited = set(source_idx)
    #         curr_steps, source_idx = bfs()
    #         steps += curr_steps + 1
    #     return steps


    # dp - top down - O(k*r**2) time; O(k*r**2) space
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        memo = {}

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        def try_lock(ring_index, key_index):
            # If we have already calculated this sub-problem, return result
            if (ring_index, key_index) in memo:
                return memo[(ring_index, key_index)]

            # If we reach the end of the keyword, it has been spelled
            if key_index == key_len:
                memo[(ring_index, key_index)] = 0
                return 0

            # For each occurence of the character key[key_index] in ring
            # calculate the minimum steps from the ring_index of ring
            min_steps = float('inf')
            for char_index in range(ring_len):
                if ring[char_index] == key[key_index]:
                    min_steps = min(min_steps,
                                    count_steps(ring_index, char_index)
                                    + 1
                                    + try_lock(char_index, key_index + 1))
            memo[(ring_index, key_index)] = min_steps
            return min_steps

        return try_lock(0, 0)


    # dp - bottom up - O(k*r**2) time; O(k*r) space
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        # Initialize values of best_steps to largest integer
        dp = [[float('inf')] * (key_len + 1) for _ in range(ring_len)]

        # Initialize the last column to 0 to represent the word has been spelled
        for row in dp:
            row[key_len] = 0

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        # For each occurence of the character at key_index of key in ring
        # stores minimum steps to the character from the ring_index of ring
        for key_index in range(key_len - 1, -1, -1):
            for ring_index in range(ring_len):
                for char_index in range(ring_len):
                    if ring[char_index] == key[key_index]:
                        dp[ring_index][key_index] = min(dp[ring_index][key_index],
                                                        count_steps(ring_index, char_index)
                                                        + 1
                                                        + dp[char_index][key_index + 1])
        return dp[0][0]


    # dp - bottom up - space optimized - O(k*r**2) time; O(r) space
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        prev = [0] * ring_len

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        for key_index in range(key_len - 1, -1, -1):
            print(prev)
            curr = [float('inf')] * ring_len
            for ring_index in range(ring_len):
                for char_index in range(ring_len):
                    if ring[char_index] == key[key_index]:
                        curr[ring_index] = min(curr[ring_index],
                                                count_steps(ring_index, char_index)
                                                + 1
                                                + prev[char_index])
            prev = curr
        return prev[0]


    # shortest path - Dijkstra's
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        # HashMap to store the indices of occurences
        # of each character in the ring
        character_indices = defaultdict(list)
        for i, char in enumerate(ring):
            character_indices[char].append(i)

        # Initialize the heap (priority queue) with the starting point
        # Each element of the heap is a tuple of integers representing:
        # totalSteps, ringIndex, keyIndex
        heap = [(0, 0, 0)]
        # tuple in seen: (ringIndex, keyIndex)
        seen = set()

        # Spell the keyword using the metal dial
        while heap:
            # Pop the element with the smallest total steps from the heap
            total_steps, ring_index, key_index = heapq.heappop(heap)

            # We have spelled the keyword
            if key_index == key_len:
                break

            # Continue if we have visited this character
            # from this position in ring before
            if (ring_index, key_index) in seen:
                continue

            # Otherwise, add this pair to the visited list
            seen.add((ring_index, key_index))

            # Add the rest of the occurences
            # of this character in ring to the heap
            for next_index in character_indices[key[key_index]]:
                heapq.heappush(heap,
                                (total_steps + count_steps(ring_index, next_index),
                                 next_index, key_index + 1))

        # Return the total steps and add keyLen to account for
        # pressing the center button for each character in the keyword
        return total_steps + key_len 
