'''

LeetCode 876: Middle of the Linked List
Approach: Fast and Slow Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 3

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 4

'''

def middleNode(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow