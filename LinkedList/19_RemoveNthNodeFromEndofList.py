'''

LeetCode 19: Remove Nth Node From End of List
Approach: Two Pointers with Dummy Node
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a linked list, remove the n-th node
from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

'''

def removeNthFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next