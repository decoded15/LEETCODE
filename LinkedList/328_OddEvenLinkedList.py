'''
LeetCode 328: Odd Even Linked List
Approach: Two Pointer Chains (Odd & Even)
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices.

The relative order within the odd and even groups must be preserved.
Indexing is 1-based.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4
'''

def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head
        return head