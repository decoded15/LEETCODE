'''
LeetCode 1721: Swapping Nodes in a Linked List
Approach: Two-Pointer Gap Technique
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a linked list and an integer k,
swap the kth node from the beginning with the kth node from the end.

The solution:
1. Move a pointer to the kth node from the start.
2. Use a two-pointer technique to find the kth node from the end.
3. Swap their values.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 4 -> 3 -> 2 -> 5
'''

def swapNodes(self, head, k):
        first = head
        second = head

        for _ in range(k - 1):
            first = first.next

        kth_from_start = first

        while first.next:
            first = first.next
            second = second.next

        kth_from_end = second

        kth_from_start.val, kth_from_end.val = (
            kth_from_end.val,
            kth_from_start.val,
        )

        return head