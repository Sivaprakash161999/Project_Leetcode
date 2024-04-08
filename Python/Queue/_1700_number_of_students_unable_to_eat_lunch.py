from typing import List
from collections import deque


class Solution:
    # queue - O(n) time; O(n) spac
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = {0:0, 1:0}
        for i in students:
            count[i] += 1
        print(count)
        while sandwiches:
            if students[0] == sandwiches[0]:
                count[students[0]] -= 1
                students.popleft()
                sandwiches.popleft()
                # print(students, sandwiches)
            elif count[sandwiches[0]] > 0:
                students.append(students.popleft())
            else:
                return len(students)
        return 0

    # counter - o(n) time; O(n) space
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        count = {0:0, 1:0}
        for i in students:
            count[i] += 1
        for i in range(n):
            if count[sandwiches[i]] == 0:
                return n - i
            count[sandwiches[i]] -= 1
        return 0



        