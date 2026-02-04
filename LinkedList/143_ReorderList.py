'''
LeetCode 143: Reorder List
Approach: Find Middle + Reverse Second Half + Merge Alternately
Time Complexity: O(n)
Space Complexity: O(1)

Reorder a linked list from:
L0 → L1 → L2 → … → Ln
to
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

The solution involves splitting the list, reversing the second half,
and merging the two halves alternately in-place.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
'''

def reorderList(self, head):
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2