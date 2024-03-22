from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterative - O(n) time; O(1) space
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # recursive - O(n) time; O(n) space
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head.next
        curr = head
        # print(curr.val, tail.val)
        head = self.reverseList(head.next)
        # print(head.val)
        # print(curr.val, curr.next.val, tail.val)
        curr.next = None
        tail.next = curr
        return head

    # stack
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        stack = []
        while head:
            stack.append(head)
            head = head.next
        new_head = stack.pop()
        current = new_head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None
        return new_head

        