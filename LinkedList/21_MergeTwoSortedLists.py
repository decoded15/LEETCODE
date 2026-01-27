'''

LeetCode 21: Merge Two Sorted Lists
Approach: Two Pointers with Dummy Node
Time Complexity: O(n + m)
Space Complexity: O(1)

You are given the heads of two sorted linked lists l1 and l2.
Merge the two lists into one sorted list and return the head
of the merged linked list.

The list should be made by splicing together the nodes
of the first two lists.

Example:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''

def mergeTwoLists(l1, l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next