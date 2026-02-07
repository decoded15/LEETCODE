'''
LeetCode 24: Swap Nodes in Pairs
Approach: Iterative Pairwise Pointer Swapping with Dummy Node
Time Complexity: O(n)
Space Complexity: O(1)

Given a singly linked list, swap every two adjacent nodes and return the modified list.
You must swap the nodes themselves, not their values.

The solution iterates through the list using a dummy node and swaps nodes in pairs
by adjusting pointers in-place.

Example:
Input: 1 -> 2 -> 3 -> 4
Output: 2 -> 1 -> 4 -> 3
'''

def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        return dummy.next