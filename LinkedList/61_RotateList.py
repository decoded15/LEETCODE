'''
LeetCode 61: Rotate List
Approach: Circular Linked List + Break at Correct Position
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a linked list, rotate the list to the right by k places.

The solution:
1. Compute the length of the list.
2. Connect the tail to the head to form a circular list.
3. Find the new tail at position (length - k % length - 1).
4. Break the circle to form the rotated list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 4 -> 5 -> 1 -> 2 -> 3
'''

def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head

        k = k % length
        steps_to_new_tail = length - k - 1

        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head