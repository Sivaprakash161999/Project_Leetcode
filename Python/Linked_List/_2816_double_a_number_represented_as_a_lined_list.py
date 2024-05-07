from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0:
            return head
        number = 0
        curr = head
        while curr:
            number = (number * 10) + curr.val
            curr = curr.next
        number *= 2
        prev = None
        while number:
            curr = ListNode(number % 10)
            curr.next = prev
            prev = curr
            number //= 10
        return prev

    # stack - O(n) time; O(n) space
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0:
            return head
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        carry = 0
        prev = None
        while stack:
            val = (stack.pop() * 2) + carry
            node_val = val % 10
            carry = val // 10
            curr = ListNode(node_val)
            prev, curr.next = curr, prev
        if carry:
            curr = ListNode(carry)
            prev, curr.next = curr, prev
        return prev

    # inplace - O(n) time; O(1) space
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr.val > 4:
            head = ListNode(1, curr)
        while curr.next:
            curr.val = (2 * curr.val + (curr.next.val > 4)) % 10
            curr = curr.next
        curr.val = (curr.val * 2) % 10
        return head