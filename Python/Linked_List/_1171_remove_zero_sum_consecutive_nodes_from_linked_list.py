from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # hash map + stack + prefix sum - O(n) time; O(n) space
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []  # (sum_up_to_node, node)
        cur_sum = 0
        seen_sum = set()
        while head:
            cur_sum += head.val
            if cur_sum == 0:
                stack = []
                seen_sum = set()
            elif cur_sum in seen_sum:
                while stack and stack[-1][0] != cur_sum:
                    old_sum, _ = stack.pop()
                    seen_sum.remove(old_sum)
            else:
                seen_sum.add(cur_sum)
                stack.append([cur_sum, head])
            head = head.next
        if not stack:
            return None
        head = tmp = stack[0][1]
        head.next = None
        for i in range(1, len(stack)):
            node = stack[i][1]
            node.next = None
            tmp.next = node
            tmp = tmp.next
        return head      

    # linked list + prefix sum - O(n^2) time; O(1) space
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front

        while start is not None:
            prefix_sum = 0
            end = start.next

            while end is not None:
                # Add end's value to the prefix sum
                prefix_sum += end.val
                # Delete zero sum consecutive sequence
                # by setting node before sequence to node after
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next 

    # prefix sum hash table - 2 pass (excatly)
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {0: front}

        # calculate the prefix sum for each node and add to the hashmap
        # Duplicate prefix sum values will be replaced
        while current is not None:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        # Reset prefix sum and current
        prefix_sum = 0
        current = front

        # Delete zero sum consecutive sequences
        # by setting node before sequence to node after
        while current is not None:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        return front.next

    # prefix sum hashtable - 2 pass(almost); O(n) time; O(n) space 
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            # Add current's value to the prefix sum
            prefix_sum += current.val

            # If prefix_sum is already in the hashmap,
            # we have found a zero-sum sequence:
            if prefix_sum in prefix_sum_to_node:
                prev = prefix_sum_to_node[prefix_sum]
                current = prev.next

                # Delete zero sum nodes from hashmap
                # to prevent incorrect deletions from linked list
                p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    current = current.next
                    p += current.val

                # Make connection from the node before
                # the zero sum sequence to the node after
                prev.next = current.next
            else:
                # Add new prefix_sum to hashmap
                prefix_sum_to_node[prefix_sum] = current
            
            # Progress to next element in list
            current = current.next
        return front.next
