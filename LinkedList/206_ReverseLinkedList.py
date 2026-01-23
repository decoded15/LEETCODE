'''

LeetCode 206: Reverse Linked List
Approach: Iterative Pointer Manipulation (prev, curr, next)
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a singly linked list,
reverse the list and return the new head.

Example:
Input: 1 -> 2 -> 3 -> 4 -> None
Output: 4 -> 3 -> 2 -> 1 -> None

'''

def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev