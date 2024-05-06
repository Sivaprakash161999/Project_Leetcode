


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    # monotonic stack - O(n) time; O(n) space
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                last = stack.pop()
            stack.append(curr)
            curr = curr.next
        
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        return stack[0]

    # recursion - O(n) time; O(n) space
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        nexts = self.removeNodes(head.next)
        if head.val < nexts.val:
            return nexts
        head.next = nexts
        return head

    # iterative reversal - O(n) time; O(1) space
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        rev_head = reverse(head)
        prev = rev_head
        curr = rev_head.next
        while curr:
            if prev.val > curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return reverse(rev_head)
