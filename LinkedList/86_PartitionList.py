'''
LeetCode 86: Partition List
Approach: Two Dummy Lists (Before & After Partition)
Time Complexity: O(n)
Space Complexity: O(1)

Given the head of a linked list and a value x,
rearrange the list so that all nodes with values less than x
come before nodes with values greater than or equal to x.

The relative order of nodes in each partition must be preserved.

The solution:
1. Create two dummy lists: one for values < x and one for values >= x.
2. Traverse the original list once.
3. Attach nodes to the appropriate list.
4. Connect the two lists at the end.

Example:
Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
'''

def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next