from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Recursion
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(node):
            if not node:
                return None, 0
            sub_node, count = rec(node.next)
            if count == n - 1:
                node.next = None
                return sub_node, count + 1
            else:
                node.next = sub_node
                return node, count + 1
        return rec(head)[0]
                
    # Recursion - Stack
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        head = None
        count = 0
        prev = None
        while stack:
            prev = head
            head = stack.pop()
            count += 1
            if count == n:
                head.next = None
                head = prev
            else:
                head.next = prev
            
        return head

    # Two-Pointers
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next
        