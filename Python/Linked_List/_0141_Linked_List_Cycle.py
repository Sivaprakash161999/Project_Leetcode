from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # hash set - time: O(n), space: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # print(pos)
        visit = set()
        if not head:
            return False
        while head:
            if head in visit:
                return True
            visit.add(head)
            head = head.next
        return False

    # two pointer - slow and fast - time: O(n), space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head
        i = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    