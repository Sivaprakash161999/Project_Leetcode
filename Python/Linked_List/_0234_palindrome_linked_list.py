from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # using list: O(n) time, O(n) space
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        n = len(ls)
        for i in range(n // 2):
            if ls[i] != ls[n - i - 1]:
                return False
        return True

    # fast and slow pointer and reversing 2nd half of list
    # O(n) time; O(1) space
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
        